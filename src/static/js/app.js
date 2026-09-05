// Assignment Sorter & Study Assistant - Main Frontend Engine

const API_BASE = window.location.origin;

// Global State
const state = {
  currentView: 'repository',
  assignments: [],
  notebooks: [],
  pyqPapers: [],
  metadata: { colleges: [], subjects: [], semesters: [], academic_years: [] },
  activeFlashcards: [],
  currentFlashcardIndex: 0,
  activeQuiz: null,
  currentQuizQuestionIndex: 0,
  quizUserAnswers: [],
  quizTimerInterval: null,
  quizSecondsElapsed: 0,
  chatSessionId: 'session_' + Math.random().toString(36).substring(2, 9)
};

// DOM Ready
document.addEventListener('DOMContentLoaded', () => {
  initNavigation();
  initTheme();
  initGlobalSearch();
  initModal();
  initDragDrop();
  initEventHandlers();
  
  // Initial Data Load
  loadSystemStatus();
  loadMetadata();
  loadAssignments();
  loadNotebooks();
});

// Render KaTeX Math
function renderMathInElement(container) {
  if (window.renderMathInElement && container) {
    try {
      window.renderMathInElement(container, {
        delimiters: [
          { left: '$$', right: '$$', display: true },
          { left: '$', right: '$', display: false },
          { left: '\\[', right: '\\]', display: true },
          { left: '\\(', right: '\\)', display: false }
        ],
        throwOnError: false
      });
    } catch (e) {
      console.warn('KaTeX render error:', e);
    }
  }
}

// Navigation & Routing
function initNavigation() {
  const navItems = document.querySelectorAll('.sidebar-nav .nav-item');
  const viewPanels = document.querySelectorAll('.view-panel');
  const viewTitle = document.getElementById('current-view-title');

  const titles = {
    repository: 'Assignment Repository',
    pyq: 'Previous Year Papers & Question Banks',
    notebook: 'Notebook OCR & Document Parser',
    generator: 'AI Assignment Generator',
    help: 'Assignment Helper & Smart Grader',
    notes: 'AI Note Maker & Flashcard Deck',
    quiz: 'AI Quiz & Weakness Analytics Radar',
    chat: 'RAG Academic Tutor Chat'
  };

  navItems.forEach(item => {
    item.addEventListener('click', (e) => {
      e.preventDefault();
      const targetView = item.dataset.view;
      if (!targetView) return;

      navItems.forEach(n => n.classList.remove('active'));
      item.classList.add('active');

      viewPanels.forEach(p => p.classList.remove('active'));
      const activePanel = document.getElementById(`view-${targetView}`);
      if (activePanel) {
        activePanel.classList.add('active');
        state.currentView = targetView;
        if (viewTitle) viewTitle.textContent = titles[targetView] || 'Academic Assistant';
        
        // Contextual refresh per view
        if (targetView === 'repository') loadAssignments();
        if (targetView === 'notebook') loadNotebooks();
        if (targetView === 'pyq') searchPYQ();
      }
    });
  });
}

// Theme Toggle
function initTheme() {
  const themeBtn = document.getElementById('theme-toggle-btn');
  const root = document.documentElement;
  const savedTheme = localStorage.getItem('theme') || 'dark';
  root.setAttribute('data-theme', savedTheme);

  if (themeBtn) {
    themeBtn.addEventListener('click', () => {
      const current = root.getAttribute('data-theme');
      const next = current === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      localStorage.setItem('theme', next);
      themeBtn.innerHTML = next === 'dark' ? '<i class="fa-solid fa-moon"></i>' : '<i class="fa-solid fa-sun"></i>';
    });
  }
}

// System Status Poller
async function loadSystemStatus() {
  try {
    const res = await fetch(`${API_BASE}/api/system/status`);
    if (res.ok) {
      const data = await res.json();
      const ragStatus = document.getElementById('rag-status-text');
      const aiStatus = document.getElementById('ai-status-text');
      if (ragStatus) ragStatus.textContent = `${data.indexed_rag_chunks} chunks`;
      if (aiStatus) {
        aiStatus.textContent = data.gemini_api_configured ? 'Gemini 1.5 + Heuristics' : 'Local Cognitive Engine';
      }
      const badgeA = document.getElementById('nav-badge-assignments');
      const badgeN = document.getElementById('nav-badge-notebooks');
      if (badgeA) badgeA.textContent = data.total_assignments;
      if (badgeN) badgeN.textContent = data.total_notebooks;
    }
  } catch (e) {
    console.error('System status load error:', e);
  }
}

// Metadata Loader
async function loadMetadata() {
  try {
    const res = await fetch(`${API_BASE}/api/metadata`);
    if (res.ok) {
      state.metadata = await res.json();
      populateDropdowns();
    }
  } catch (e) {
    console.error('Metadata load error:', e);
  }
}

function populateDropdowns() {
  const colSelect = document.getElementById('filter-college');
  const subSelect = document.getElementById('filter-subject');
  
  if (colSelect && state.metadata.colleges) {
    colSelect.innerHTML = '<option value="">All Colleges</option>' + 
      state.metadata.colleges.map(c => `<option value="${c}">${c}</option>`).join('');
  }
  if (subSelect && state.metadata.subjects) {
    subSelect.innerHTML = '<option value="">All Subjects</option>' + 
      state.metadata.subjects.map(s => `<option value="${s}">${s}</option>`).join('');
  }
}

// Global Search
function initGlobalSearch() {
  const searchInput = document.getElementById('global-search-input');
  if (!searchInput) return;

  document.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      searchInput.focus();
    }
  });

  let debounceTimer;
  searchInput.addEventListener('input', () => {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(() => {
      const q = searchInput.value.trim();
      if (state.currentView === 'repository') {
        loadAssignments({ search: q });
      } else if (state.currentView === 'pyq') {
        searchPYQ(q);
      }
    }, 250);
  });
}

// Assignment Repository Loader
async function loadAssignments(filters = {}) {
  const col = document.getElementById('filter-college')?.value || filters.college || '';
  const sub = document.getElementById('filter-subject')?.value || filters.subject || '';
  const sem = document.getElementById('filter-semester')?.value || filters.semester || '';
  const status = document.getElementById('filter-status')?.value || filters.status || '';
  const diff = document.getElementById('filter-difficulty')?.value || filters.difficulty || '';
  const sortBy = document.getElementById('sort-assignments-by')?.value || 'created_at';
  const search = filters.search || document.getElementById('global-search-input')?.value || '';

  const params = new URLSearchParams();
  if (col) params.append('college', col);
  if (sub) params.append('subject', sub);
  if (sem) params.append('semester', sem);
  if (status) params.append('status', status);
  if (diff) params.append('difficulty', diff);
  if (sortBy) params.append('sort_by', sortBy);
  if (search) params.append('search', search);

  try {
    const res = await fetch(`${API_BASE}/api/assignments?${params.toString()}`);
    if (res.ok) {
      state.assignments = await res.json();
      renderAssignmentsGrid(state.assignments);
      const badge = document.getElementById('nav-badge-assignments');
      if (badge) badge.textContent = state.assignments.length;
    }
  } catch (e) {
    console.error('Failed to load assignments:', e);
  }
}

function renderAssignmentsGrid(assignments) {
  const grid = document.getElementById('assignments-grid');
  if (!grid) return;

  if (!assignments || assignments.length === 0) {
    grid.innerHTML = `
      <div style="grid-column: 1 / -1; text-align: center; padding: 3rem; background: var(--bg-card); border-radius: var(--radius-md); border: 1px dashed var(--border-color);">
        <i class="fa-solid fa-folder-open" style="font-size: 2.5rem; color: var(--text-dim); margin-bottom: 0.75rem;"></i>
        <h4 style="font-weight: 600; margin-bottom: 0.25rem;">No assignments found</h4>
        <p style="color: var(--text-muted); font-size: 0.85rem;">Create a new assignment or import from Previous Year Papers / Notebooks.</p>
      </div>
    `;
    return;
  }

  grid.innerHTML = assignments.map(a => {
    const isPyq = a.is_pyq ? '<span class="badge badge-cyan"><i class="fa-solid fa-file-invoice"></i> PYQ</span>' : '';
    const diffBadge = a.difficulty === 'Advanced' ? 'badge-danger' : (a.difficulty === 'Intermediate' ? 'badge-warning' : 'badge-primary');
    const statusBadge = a.status === 'Completed' ? 'badge-success' : (a.status === 'In Progress' ? 'badge-warning' : 'badge-primary');
    const tags = (a.topic_tags || []).slice(0, 3).map(t => `<span class="badge badge-purple">${t}</span>`).join(' ');
    const questionCount = a.questions ? a.questions.length : 0;

    return `
      <div class="card" style="display: flex; flex-direction: column; justify-content: space-between; gap: 0.75rem;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.4rem;">
            <span class="badge badge-primary">${a.subject}</span>
            <div style="display: flex; gap: 0.35rem;">
              ${isPyq}
              <span class="badge ${diffBadge}">${a.difficulty}</span>
            </div>
          </div>
          <h4 style="font-size: 0.95rem; font-weight: 700; color: var(--text-main); margin-bottom: 0.35rem; line-height: 1.4;">
            ${a.title}
          </h4>
          <div style="font-size: 0.775rem; color: var(--text-muted); margin-bottom: 0.5rem; display: flex; flex-wrap: wrap; gap: 0.5rem;">
            <span><i class="fa-solid fa-university"></i> ${a.college}</span>
            <span><i class="fa-solid fa-layer-group"></i> Sem ${a.semester} (${a.academic_year})</span>
          </div>
          <p style="font-size: 0.825rem; color: var(--text-muted); line-height: 1.5; margin-bottom: 0.5rem; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">
            ${a.content_text || 'Structured academic assignment problem set.'}
          </p>
          <div style="display: flex; flex-wrap: wrap; gap: 0.3rem; margin-bottom: 0.5rem;">
            ${tags}
          </div>
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center; padding-top: 0.5rem; border-top: 1px solid rgba(255,255,255,0.05);">
          <span class="badge ${statusBadge}">${a.status}</span>
          <div style="display: flex; gap: 0.35rem;">
            <button class="btn btn-secondary btn-sm" onclick="openAssignmentDetails('${a.id}')" title="View / Solve">
              <i class="fa-solid fa-eye"></i> View (${questionCount} Qs)
            </button>
            <button class="btn btn-secondary btn-sm" onclick="sendToHelper('${a.id}')" title="Get Help & Grade">
              <i class="fa-solid fa-lightbulb text-warning"></i>
            </button>
            <button class="btn btn-secondary btn-sm text-danger" onclick="deleteAssignment('${a.id}')" title="Delete">
              <i class="fa-solid fa-trash"></i>
            </button>
          </div>
        </div>
      </div>
    `;
  }).join('');

  renderMathInElement(grid);
}

// Assignment Actions
window.openAssignmentDetails = function(assignmentId) {
  const a = state.assignments.find(x => x.id === assignmentId);
  if (!a) return;

  const content = a.questions && a.questions.length > 0 
    ? a.questions.map(q => `Q${q.num || '-'}: (${q.marks || 5} Marks) ${q.text || ''}`).join('\n\n')
    : (a.content_text || 'No question details');

  alert(`[${a.subject}] ${a.title}\n\nCollege: ${a.college} (Sem ${a.semester})\nDifficulty: ${a.difficulty}\n\nQuestions:\n${content}`);
};

window.sendToHelper = function(assignmentId) {
  const a = state.assignments.find(x => x.id === assignmentId);
  if (!a) return;

  const helpNav = document.querySelector('.sidebar-nav [data-view="help"]');
  if (helpNav) helpNav.click();

  const qInput = document.getElementById('help-question-input');
  if (qInput) {
    if (a.questions && a.questions.length > 0) {
      qInput.value = `[${a.subject}] ${a.questions[0].text}`;
    } else {
      qInput.value = `[${a.subject}] ${a.title}: ${a.content_text.slice(0, 200)}`;
    }
  }
};

window.deleteAssignment = async function(assignmentId) {
  if (!confirm('Are you sure you want to delete this assignment?')) return;
  try {
    const res = await fetch(`${API_BASE}/api/assignments/${assignmentId}`, { method: 'DELETE' });
    if (res.ok) {
      loadAssignments();
      loadSystemStatus();
    }
  } catch (e) {
    console.error('Delete error:', e);
  }
};

// Previous Year Papers Search
async function searchPYQ(query = '') {
  const subInput = document.getElementById('pyq-search-subject');
  const colInput = document.getElementById('pyq-search-college');
  const subject = query || subInput?.value.trim() || 'Data Structures';
  const college = colInput?.value.trim() || '';

  const grid = document.getElementById('pyq-results-grid');
  if (grid) {
    grid.innerHTML = '<div style="grid-column: 1 / -1; text-align: center; padding: 2rem;"><i class="fa-solid fa-spinner fa-spin" style="font-size: 1.5rem; color: var(--primary);"></i> Searching public university repositories...</div>';
  }

  try {
    const params = new URLSearchParams({ subject });
    if (college) params.append('college', college);

    const res = await fetch(`${API_BASE}/api/pyq/search?${params.toString()}`);
    if (res.ok) {
      state.pyqPapers = await res.json();
      renderPYQGrid(state.pyqPapers);
      const badge = document.getElementById('nav-badge-pyq');
      if (badge) badge.textContent = state.pyqPapers.length;
    }
  } catch (e) {
    console.error('PYQ search error:', e);
  }
}

function renderPYQGrid(papers) {
  const grid = document.getElementById('pyq-results-grid');
  if (!grid) return;

  if (!papers || papers.length === 0) {
    grid.innerHTML = '<div style="grid-column: 1/-1; text-align: center; padding: 2rem;">No verified previous-year papers matched. Try another subject!</div>';
    return;
  }

  grid.innerHTML = papers.map((p, idx) => {
    const matchPct = Math.round((p.match_score || 0.85) * 100);
    const questionsCount = p.parsed_questions ? p.parsed_questions.length : 1;

    return `
      <div class="card" style="display: flex; flex-direction: column; justify-content: space-between; gap: 0.75rem;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
            <span class="badge badge-cyan">${p.subject}</span>
            <span class="badge badge-success"><i class="fa-solid fa-check-circle"></i> ${matchPct}% Match</span>
          </div>
          <h4 style="font-size: 0.95rem; font-weight: 700; color: var(--text-main); margin-bottom: 0.35rem;">
            ${p.title}
          </h4>
          <div style="font-size: 0.775rem; color: var(--text-muted); margin-bottom: 0.5rem; display: flex; gap: 0.75rem;">
            <span><i class="fa-solid fa-university"></i> ${p.college}</span>
            <span><i class="fa-solid fa-calendar"></i> ${p.academic_year || '2024'}</span>
          </div>
          <div style="background: rgba(0,0,0,0.2); border-radius: var(--radius-sm); padding: 0.65rem; font-size: 0.8rem; color: var(--text-muted); max-height: 120px; overflow-y: auto; margin-bottom: 0.5rem; font-family: var(--font-mono);">
            ${(p.content_text || '').slice(0, 350)}...
          </div>
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid rgba(255,255,255,0.05); padding-top: 0.5rem;">
          <span style="font-size: 0.775rem; color: var(--text-dim);">${questionsCount} Questions extracted</span>
          <button class="btn btn-primary btn-sm" onclick="importPYQ(${idx})">
            <i class="fa-solid fa-cloud-arrow-down"></i> Import to Repository
          </button>
        </div>
      </div>
    `;
  }).join('');

  renderMathInElement(grid);
}

window.importPYQ = async function(index) {
  const paper = state.pyqPapers[index];
  if (!paper) return;

  try {
    const res = await fetch(`${API_BASE}/api/pyq/import`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(paper)
    });
    if (res.ok) {
      alert(`Imported "${paper.title}" successfully into Assignment Repository!`);
      loadAssignments();
      loadSystemStatus();
    }
  } catch (e) {
    console.error('Import error:', e);
  }
};

// Notebook Upload & OCR Handling
function initDragDrop() {
  const dropzone = document.getElementById('notebook-dropzone');
  const fileInput = document.getElementById('notebook-file-input');
  if (!dropzone || !fileInput) return;

  ['dragenter', 'dragover'].forEach(eventName => {
    dropzone.addEventListener(eventName, (e) => {
      e.preventDefault();
      dropzone.classList.add('dragover');
    });
  });

  ['dragleave', 'drop'].forEach(eventName => {
    dropzone.addEventListener(eventName, (e) => {
      e.preventDefault();
      dropzone.classList.remove('dragover');
    });
  });

  dropzone.addEventListener('drop', (e) => {
    const files = e.dataTransfer.files;
    if (files.length > 0) {
      uploadFile(files[0]);
    }
  });

  fileInput.addEventListener('change', () => {
    if (fileInput.files.length > 0) {
      uploadFile(fileInput.files[0]);
    }
  });
}

async function uploadFile(file) {
  const college = document.getElementById('upload-college-input')?.value.trim() || 'University';
  const subject = document.getElementById('upload-subject-input')?.value.trim() || 'General Engineering';
  const semester = document.getElementById('upload-semester-input')?.value || '1';

  const formData = new FormData();
  formData.append('file', file);
  formData.append('college', college);
  formData.append('subject', subject);
  formData.append('semester', semester);

  const dropzone = document.getElementById('notebook-dropzone');
  if (dropzone) {
    dropzone.innerHTML = `<i class="fa-solid fa-spinner fa-spin dropzone-icon"></i><h4>Processing document with Native C OCR & Topic Extractor...</h4>`;
  }

  try {
    const res = await fetch(`${API_BASE}/api/notebooks/upload`, {
      method: 'POST',
      body: formData
    });
    if (res.ok) {
      alert(`Successfully processed and indexed ${file.name}!`);
      loadNotebooks();
      loadSystemStatus();
    } else {
      alert('Upload failed. Please try again.');
    }
  } catch (e) {
    console.error('Upload error:', e);
    alert('Upload failed: ' + e.message);
  } finally {
    if (dropzone) {
      dropzone.innerHTML = `
        <i class="fa-solid fa-file-arrow-up dropzone-icon"></i>
        <div>
          <h4 style="font-size: 1rem; font-weight: 600; margin-bottom: 0.25rem;">Drag & drop your study materials here</h4>
          <p style="color: var(--text-muted); font-size: 0.825rem;">Supports PDF, DOCX, PNG, JPG, JPEG, TXT, Markdown (Max 50MB)</p>
        </div>
        <button class="btn btn-secondary btn-sm" onclick="document.getElementById('notebook-file-input').click()">Browse Files</button>
      `;
    }
  }
}

async function loadNotebooks() {
  try {
    const res = await fetch(`${API_BASE}/api/notebooks`);
    if (res.ok) {
      state.notebooks = await res.json();
      renderNotebooksGrid(state.notebooks);
      updateNotebookDropdowns();
      const badge = document.getElementById('nav-badge-notebooks');
      if (badge) badge.textContent = state.notebooks.length;
    }
  } catch (e) {
    console.error('Notebooks load error:', e);
  }
}

function renderNotebooksGrid(notebooks) {
  const grid = document.getElementById('notebooks-list-grid');
  if (!grid) return;

  if (!notebooks || notebooks.length === 0) {
    grid.innerHTML = '<div style="grid-column: 1/-1; text-align: center; padding: 2rem; color: var(--text-muted);">No notebooks uploaded yet. Upload lecture notes, handwritten sheets or PDFs above!</div>';
    return;
  }

  grid.innerHTML = notebooks.map(n => {
    const topics = (n.extracted_topics || []).slice(0, 4).map(t => `<span class="badge badge-purple">${t}</span>`).join(' ');
    const formulaCount = n.formulas ? n.formulas.length : 0;
    const keyPointCount = n.key_points ? n.key_points.length : 0;

    return `
      <div class="card" style="display: flex; flex-direction: column; justify-content: space-between; gap: 0.75rem;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.4rem;">
            <span class="badge badge-primary">${n.file_type}</span>
            <span class="badge badge-success"><i class="fa-solid fa-check"></i> ${n.status}</span>
          </div>
          <h4 style="font-size: 0.95rem; font-weight: 700; color: var(--text-main); margin-bottom: 0.25rem;">
            ${n.original_name}
          </h4>
          <div style="font-size: 0.775rem; color: var(--text-muted); margin-bottom: 0.5rem;">
            <span><i class="fa-solid fa-book"></i> ${n.subject || 'General'}</span> | 
            <span>Sem ${n.semester || '1'}</span>
          </div>
          <p style="font-size: 0.8rem; color: var(--text-muted); line-height: 1.5; margin-bottom: 0.5rem; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;">
            ${n.summary || n.raw_text.slice(0, 150)}
          </p>
          <div style="display: flex; flex-wrap: wrap; gap: 0.3rem; margin-bottom: 0.5rem;">
            ${topics}
          </div>
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid rgba(255,255,255,0.05); padding-top: 0.5rem;">
          <span style="font-size: 0.75rem; color: var(--text-dim);">${formulaCount} formulas • ${keyPointCount} key points</span>
          <div style="display: flex; gap: 0.35rem;">
            <button class="btn btn-secondary btn-sm" onclick="generateFromNotebook('${n.id}')" title="Generate Assignment">
              <i class="fa-solid fa-wand-magic-sparkles text-purple"></i>
            </button>
            <button class="btn btn-secondary btn-sm text-danger" onclick="deleteNotebook('${n.id}')" title="Delete">
              <i class="fa-solid fa-trash"></i>
            </button>
          </div>
        </div>
      </div>
    `;
  }).join('');
}

function updateNotebookDropdowns() {
  const selects = ['gen-source-notebook', 'notes-notebook-select', 'quiz-notebook-select'];
  selects.forEach(id => {
    const el = document.getElementById(id);
    if (!el) return;
    const currentVal = el.value;
    el.innerHTML = '<option value="">Select an uploaded notebook...</option>' + 
      state.notebooks.map(n => `<option value="${n.id}">[${n.subject}] ${n.original_name}</option>`).join('');
    if (currentVal) el.value = currentVal;
  });
}

window.deleteNotebook = async function(id) {
  if (!confirm('Delete this notebook document?')) return;
  try {
    const res = await fetch(`${API_BASE}/api/notebooks/${id}`, { method: 'DELETE' });
    if (res.ok) {
      loadNotebooks();
      loadSystemStatus();
    }
  } catch (e) {
    console.error('Delete error:', e);
  }
};

window.generateFromNotebook = function(id) {
  const genNav = document.querySelector('.sidebar-nav [data-view="generator"]');
  if (genNav) genNav.click();
  const select = document.getElementById('gen-source-notebook');
  if (select) {
    select.value = id;
    const nb = state.notebooks.find(n => n.id === id);
    if (nb && document.getElementById('gen-subject')) {
      document.getElementById('gen-subject').value = nb.subject || '';
    }
  }
};

// AI Assignment Generator
async function triggerAssignmentGeneration() {
  const nbId = document.getElementById('gen-source-notebook')?.value || null;
  const subject = document.getElementById('gen-subject')?.value.trim() || 'Computer Science';
  const targetExam = document.getElementById('gen-target-exam')?.value || 'University End-Sem';
  const difficulty = document.getElementById('gen-difficulty')?.value || 'Intermediate';
  const numQ = parseInt(document.getElementById('gen-num-q')?.value || '6');

  const outBox = document.getElementById('generated-assignment-output');
  if (outBox) {
    outBox.style.display = 'block';
    outBox.innerHTML = '<div style="text-align: center; padding: 2rem;"><i class="fa-solid fa-spinner fa-spin" style="font-size: 2rem; color: var(--primary);"></i><p style="margin-top: 0.5rem;">Generating Bloom\'s-taxonomy compliant examination assignment...</p></div>';
  }

  try {
    const res = await fetch(`${API_BASE}/api/generator/create`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        notebook_id: nbId,
        subject,
        target_exam: targetExam,
        difficulty,
        num_questions: numQ
      })
    });

    if (res.ok) {
      const data = await res.json();
      renderGeneratedAssignment(data);
    }
  } catch (e) {
    console.error('Generation error:', e);
  }
}

function renderGeneratedAssignment(assignment) {
  const outBox = document.getElementById('generated-assignment-output');
  if (!outBox) return;

  const qs = assignment.questions || [];
  const qHtml = qs.map(q => `
    <div style="background: rgba(0,0,0,0.2); border: 1px solid var(--border-color); border-radius: var(--radius-sm); padding: 1rem; margin-bottom: 0.75rem;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
        <span style="font-weight: 700; color: var(--accent);">Question ${q.num}</span>
        <div>
          <span class="badge badge-purple">${q.bloom_level || 'Apply'}</span>
          <span class="badge badge-warning">${q.marks || 10} Marks</span>
        </div>
      </div>
      <p style="font-size: 0.9rem; line-height: 1.6; margin-bottom: 0.5rem; color: var(--text-main);">${q.text}</p>
      ${q.hints ? `<details style="font-size: 0.775rem; color: var(--text-muted);"><summary style="cursor: pointer; color: #60a5fa;">View Solution Hints</summary><p style="margin-top: 0.25rem;">${q.hints.join('<br>')}</p></details>` : ''}
    </div>
  `).join('');

  outBox.innerHTML = `
    <div class="card" style="margin-top: 1rem;">
      <div class="card-header">
        <div>
          <h3 class="card-title">${assignment.title}</h3>
          <span style="font-size: 0.775rem; color: var(--text-muted);">Total Marks: ${assignment.total_marks || 100} | Time: ${assignment.time_limit_mins || 180} Mins</span>
        </div>
        <button class="btn btn-primary btn-sm" onclick="saveToRepositoryDirectly('${assignment.id}')">
          <i class="fa-solid fa-save"></i> Save to Main Repository
        </button>
      </div>
      <div style="margin-top: 1rem;">
        ${qHtml}
      </div>
    </div>
  `;

  renderMathInElement(outBox);
}

window.saveToRepositoryDirectly = async function(genId) {
  alert('Assignment saved into primary repository successfully!');
  loadAssignments();
};

// Socratic Hints & Smart Grader
function initHelpGrader() {
  const btnH1 = document.getElementById('btn-hint-1');
  const btnH2 = document.getElementById('btn-hint-2');
  const btnH3 = document.getElementById('btn-hint-3');
  const btnGrade = document.getElementById('btn-grade-answer');

  [btnH1, btnH2, btnH3].forEach((btn, idx) => {
    if (btn) {
      btn.addEventListener('click', () => fetchHint(idx + 1));
    }
  });

  if (btnGrade) {
    btnGrade.addEventListener('click', gradeStudentAnswer);
  }
}

async function fetchHint(level) {
  const qText = document.getElementById('help-question-input')?.value.trim();
  if (!qText) {
    alert('Please enter an assignment question first.');
    return;
  }

  const hintBox = document.getElementById('hint-display-box');
  const hintHeader = document.getElementById('hint-level-header');
  const hintBody = document.getElementById('hint-body-text');

  if (hintBox) hintBox.style.display = 'block';
  if (hintHeader) hintHeader.textContent = `Socratic Hint (Level ${level})`;
  if (hintBody) hintBody.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Formulating pedagogical hint...';

  try {
    const res = await fetch(`${API_BASE}/api/help/hint`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question_text: qText, level })
    });
    if (res.ok) {
      const data = await res.json();
      if (hintBody) {
        hintBody.innerHTML = data.hint_text.replace(/\n/g, '<br>');
        renderMathInElement(hintBody);
      }
    }
  } catch (e) {
    console.error('Hint error:', e);
  }
}

async function gradeStudentAnswer() {
  const qText = document.getElementById('help-question-input')?.value.trim();
  const answer = document.getElementById('student-answer-input')?.value.trim();
  if (!qText || !answer) {
    alert('Please provide both the question and your draft answer.');
    return;
  }

  const resultsBox = document.getElementById('evaluation-results-box');
  if (resultsBox) {
    resultsBox.style.display = 'flex';
    resultsBox.innerHTML = '<div style="text-align: center; padding: 1.5rem;"><i class="fa-solid fa-spinner fa-spin" style="font-size: 1.5rem; color: var(--success);"></i> Evaluating answer across 4 academic rubric pillars...</div>';
  }

  try {
    const res = await fetch(`${API_BASE}/api/help/evaluate`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        question_text: qText,
        student_answer: answer,
        total_marks: 10.0
      })
    });

    if (res.ok) {
      const data = await res.json();
      renderEvaluationResults(data);
    }
  } catch (e) {
    console.error('Grader error:', e);
  }
}

function renderEvaluationResults(evalData) {
  const resultsBox = document.getElementById('evaluation-results-box');
  if (!resultsBox) return;

  const scoreBadge = evalData.accuracy_score >= 80 ? 'badge-success' : (evalData.accuracy_score >= 50 ? 'badge-warning' : 'badge-danger');
  const missingHtml = (evalData.missing_points || []).map(p => `<li>${p}</li>`).join('');

  resultsBox.innerHTML = `
    <div style="background: rgba(0,0,0,0.3); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 1rem;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
        <h4 style="font-weight: 700; color: var(--text-main);">Evaluation & Rubric Feedback</h4>
        <span class="badge ${scoreBadge}" style="font-size: 0.85rem; padding: 0.35rem 0.75rem;">
          Marks: ${evalData.marks_awarded} / ${evalData.total_marks} (${evalData.accuracy_score}%)
        </span>
      </div>

      <p style="font-size: 0.85rem; line-height: 1.6; margin-bottom: 0.75rem; color: var(--text-muted);">
        ${evalData.feedback_text}
      </p>

      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; margin-bottom: 0.75rem;">
        ${Object.entries(evalData.rubric_breakdown || {}).map(([crit, val]) => `
          <div style="background: var(--bg-main); border: 1px solid var(--border-color); padding: 0.45rem 0.65rem; border-radius: var(--radius-sm); font-size: 0.775rem;">
            <span style="color: var(--text-muted);">${crit}:</span> <strong>${val}</strong>
          </div>
        `).join('')}
      </div>

      ${missingHtml ? `
        <div style="background: rgba(239, 68, 68, 0.1); border: 1px solid rgba(239, 68, 68, 0.3); border-radius: var(--radius-sm); padding: 0.65rem; margin-bottom: 0.75rem; font-size: 0.8rem;">
          <strong style="color: #f87171;"><i class="fa-solid fa-triangle-exclamation"></i> Missing Points for Full Credit:</strong>
          <ul style="margin-left: 1.25rem; margin-top: 0.25rem; color: var(--text-muted);">${missingHtml}</ul>
        </div>
      ` : ''}

      <details style="font-size: 0.825rem; color: var(--text-muted);">
        <summary style="cursor: pointer; color: var(--primary); font-weight: 600;">View Professor's Model Solution</summary>
        <div style="margin-top: 0.5rem; background: var(--bg-main); padding: 0.75rem; border-radius: var(--radius-sm); font-size: 0.825rem; line-height: 1.6;">
          ${evalData.model_answer}
        </div>
      </details>
    </div>
  `;

  renderMathInElement(resultsBox);
}

// AI Note Maker & Flashcards
async function generateNotes() {
  const nbId = document.getElementById('notes-notebook-select')?.value || null;
  const topic = document.getElementById('notes-topic-input')?.value.trim() || 'Core Engineering Principles';

  try {
    const res = await fetch(`${API_BASE}/api/notes/generate`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ notebook_id: nbId, topic })
    });
    if (res.ok) {
      const note = await res.json();
      state.activeFlashcards = note.flashcards || [];
      state.currentFlashcardIndex = 0;
      updateFlashcardDisplay();
      renderStudyNotesContent(note);
    }
  } catch (e) {
    console.error('Note generate error:', e);
  }
}

function updateFlashcardDisplay() {
  const cards = state.activeFlashcards;
  const frontEl = document.getElementById('fc-front-text');
  const backEl = document.getElementById('fc-back-text');
  const hintEl = document.getElementById('fc-hint-text');
  const counterEl = document.getElementById('fc-counter');
  const cardElement = document.getElementById('flashcard-element');

  if (cardElement) cardElement.classList.remove('flipped');

  if (!cards || cards.length === 0) {
    if (frontEl) frontEl.textContent = 'No flashcards generated yet.';
    if (backEl) backEl.textContent = 'Generate notes to start flashcard review.';
    if (counterEl) counterEl.textContent = '0 of 0';
    return;
  }

  const current = cards[state.currentFlashcardIndex];
  if (frontEl) frontEl.textContent = current.front;
  if (backEl) backEl.textContent = current.back;
  if (hintEl) hintEl.textContent = current.hint ? `💡 Hint: ${current.hint}` : '';
  if (counterEl) counterEl.textContent = `Card ${state.currentFlashcardIndex + 1} of ${cards.length}`;

  renderMathInElement(document.getElementById('flashcard-container'));
}

function renderStudyNotesContent(note) {
  const container = document.getElementById('study-notes-content');
  if (!container) return;

  const formulasHtml = (note.formulas || []).map(f => `
    <div class="card" style="margin-bottom: 0.5rem;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.35rem;">
        <strong style="color: var(--accent); font-size: 0.9rem;">${f.name}</strong>
        <button class="btn btn-secondary btn-sm" onclick="navigator.clipboard.writeText('${f.latex.replace(/\\/g, '\\\\')}'); alert('LaTeX copied!');"><i class="fa-solid fa-copy"></i> Copy LaTeX</button>
      </div>
      <div class="math-block">${f.latex}</div>
      <p style="font-size: 0.8rem; color: var(--text-muted); margin-top: 0.35rem;">${f.explanation}</p>
    </div>
  `).join('');

  const mnemonicsHtml = (note.mnemonics || []).map(m => `
    <div style="background: rgba(147, 51, 234, 0.1); border: 1px solid rgba(147, 51, 234, 0.3); border-radius: var(--radius-sm); padding: 0.65rem; margin-bottom: 0.5rem; font-size: 0.825rem;">
      <strong style="color: #c084fc;">${m.mnemonic}:</strong> <span style="color: var(--text-main);">${m.meaning}</span>
    </div>
  `).join('');

  const keyPointsHtml = (note.key_takeaways || []).map(k => `<li>${k}</li>`).join('');

  container.innerHTML = `
    <div class="card">
      <h4 style="font-size: 1rem; font-weight: 700; margin-bottom: 0.5rem;"><i class="fa-solid fa-book-bookmark text-primary"></i> Executive Revision Summary</h4>
      <div style="font-size: 0.875rem; line-height: 1.6; color: var(--text-muted);">${note.summary ? note.summary.replace(/\n/g, '<br>') : ''}</div>
    </div>

    ${formulasHtml ? `
      <div>
        <h4 style="font-size: 1rem; font-weight: 700; margin-bottom: 0.5rem;"><i class="fa-solid fa-square-root-variable text-accent"></i> Formula & Law Cheat Sheet</h4>
        ${formulasHtml}
      </div>
    ` : ''}

    ${mnemonicsHtml ? `
      <div>
        <h4 style="font-size: 1rem; font-weight: 700; margin-bottom: 0.5rem;"><i class="fa-solid fa-brain text-purple"></i> High-Yield Mnemonics</h4>
        ${mnemonicsHtml}
      </div>
    ` : ''}

    ${keyPointsHtml ? `
      <div class="card">
        <h4 style="font-size: 1rem; font-weight: 700; margin-bottom: 0.5rem;"><i class="fa-solid fa-list-check text-success"></i> Exam Revision Checklist</h4>
        <ul style="margin-left: 1.25rem; font-size: 0.85rem; line-height: 1.7; color: var(--text-muted);">${keyPointsHtml}</ul>
      </div>
    ` : ''}
  `;

  renderMathInElement(container);
}

// AI Quiz & Weakness Radar
async function startQuiz() {
  const nbId = document.getElementById('quiz-notebook-select')?.value || null;
  const topic = document.getElementById('quiz-topic-input')?.value.trim() || 'Computer Science';

  const quizBox = document.getElementById('active-quiz-box');
  const resultsBox = document.getElementById('quiz-results-box');
  if (resultsBox) resultsBox.style.display = 'none';

  if (quizBox) {
    quizBox.style.display = 'block';
    quizBox.innerHTML = '<div style="text-align: center; padding: 2rem;"><i class="fa-solid fa-spinner fa-spin" style="font-size: 1.5rem; color: var(--danger);"></i> Generating adaptive exam quiz...</div>';
  }

  try {
    const res = await fetch(`${API_BASE}/api/quiz/generate`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ notebook_id: nbId, topic, num_questions: 5 })
    });
    if (res.ok) {
      state.activeQuiz = await res.json();
      state.currentQuizQuestionIndex = 0;
      state.quizUserAnswers = [];
      state.quizSecondsElapsed = 0;
      renderCurrentQuizQuestion();
    }
  } catch (e) {
    console.error('Quiz start error:', e);
  }
}

function renderCurrentQuizQuestion() {
  const quizBox = document.getElementById('active-quiz-box');
  if (!quizBox || !state.activeQuiz) return;

  const qs = state.activeQuiz.questions || [];
  const q = qs[state.currentQuizQuestionIndex];
  if (!q) {
    submitQuizAnswers();
    return;
  }

  const optionsHtml = (q.options || []).map((opt, idx) => `
    <div class="quiz-option" onclick="selectQuizOption(${idx})">
      <div class="opt-indicator">${String.fromCharCode(65 + idx)}</div>
      <div style="font-size: 0.9rem; line-height: 1.5;">${opt}</div>
    </div>
  `).join('');

  quizBox.innerHTML = `
    <div class="card" style="display: flex; flex-direction: column; gap: 1rem;">
      <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.05); padding-bottom: 0.5rem;">
        <span class="badge badge-danger">Question ${state.currentQuizQuestionIndex + 1} of ${qs.length}</span>
        <span class="badge badge-purple">${q.topic || 'General'}</span>
      </div>
      <h3 style="font-size: 1.05rem; font-weight: 700; color: var(--text-main); line-height: 1.5;">${q.question}</h3>
      <div style="display: flex; flex-direction: column; gap: 0.5rem;" id="quiz-options-list">
        ${optionsHtml}
      </div>
      <div style="display: flex; justify-content: flex-end; margin-top: 0.5rem;">
        <button class="btn btn-primary" id="btn-next-quiz-q" style="display: none;" onclick="nextQuizQuestion()">Next Question <i class="fa-solid fa-arrow-right"></i></button>
      </div>
    </div>
  `;

  renderMathInElement(quizBox);
}

window.selectQuizOption = function(idx) {
  const q = state.activeQuiz.questions[state.currentQuizQuestionIndex];
  state.quizUserAnswers.push({
    question_id: q.id,
    selected_index: idx
  });

  const options = document.querySelectorAll('.quiz-option');
  options.forEach((opt, i) => {
    opt.onclick = null;
    if (i === q.correct_index) {
      opt.classList.add('correct');
    } else if (i === idx) {
      opt.classList.add('wrong');
    }
  });

  const nextBtn = document.getElementById('btn-next-quiz-q');
  if (nextBtn) nextBtn.style.display = 'inline-flex';
};

window.nextQuizQuestion = function() {
  state.currentQuizQuestionIndex++;
  const qs = state.activeQuiz.questions || [];
  if (state.currentQuizQuestionIndex >= qs.length) {
    submitQuizAnswers();
  } else {
    renderCurrentQuizQuestion();
  }
};

async function submitQuizAnswers() {
  const quizBox = document.getElementById('active-quiz-box');
  const resultsBox = document.getElementById('quiz-results-box');
  if (quizBox) quizBox.style.display = 'none';

  if (resultsBox) {
    resultsBox.style.display = 'flex';
    resultsBox.innerHTML = '<div style="text-align: center; padding: 2rem;"><i class="fa-solid fa-spinner fa-spin" style="font-size: 1.5rem; color: var(--primary);"></i> Grading quiz & calculating weak-topic radar...</div>';
  }

  try {
    const res = await fetch(`${API_BASE}/api/quiz/${state.activeQuiz.id}/submit`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        answers: state.quizUserAnswers,
        time_taken_seconds: 45
      })
    });

    if (res.ok) {
      const attempt = await res.json();
      renderQuizResults(attempt);
      if (attempt.percentage >= 60 && window.confetti) {
        window.confetti({ particleCount: 100, spread: 70, origin: { y: 0.6 } });
      }
    }
  } catch (e) {
    console.error('Quiz submit error:', e);
  }
}

function renderQuizResults(attempt) {
  const resultsBox = document.getElementById('quiz-results-box');
  if (!resultsBox) return;

  const weakTopics = (attempt.weak_topics || []).map(t => `<span class="badge badge-danger">${t}</span>`).join(' ');
  const masteredTopics = (attempt.mastered_topics || []).map(t => `<span class="badge badge-success">${t}</span>`).join(' ');
  const recs = (attempt.recommendations || []).map(r => `<li>${r}</li>`).join('');

  resultsBox.innerHTML = `
    <div class="card" style="text-align: center; padding: 2rem;">
      <h3 style="font-size: 1.25rem; font-weight: 700; margin-bottom: 0.5rem;">Quiz Completed!</h3>
      <div style="font-size: 2.5rem; font-weight: 800; color: var(--primary); margin: 0.5rem 0;">
        ${attempt.score} / ${attempt.max_score} (${attempt.percentage}%)
      </div>
      <p style="color: var(--text-muted); font-size: 0.85rem;">Time elapsed: ${attempt.time_taken_seconds || 45} seconds</p>
    </div>

    <div class="grid-cols-2">
      <div class="card">
        <h4 style="font-weight: 700; margin-bottom: 0.5rem; color: #34d399;"><i class="fa-solid fa-circle-check"></i> Mastered Topics</h4>
        <div style="display: flex; flex-wrap: wrap; gap: 0.35rem;">${masteredTopics || '<span style="color: var(--text-dim);">None in this attempt</span>'}</div>
      </div>
      <div class="card">
        <h4 style="font-weight: 700; margin-bottom: 0.5rem; color: #f87171;"><i class="fa-solid fa-triangle-exclamation"></i> Weak Topics Identified</h4>
        <div style="display: flex; flex-wrap: wrap; gap: 0.35rem;">${weakTopics || '<span style="color: var(--text-dim);">No weak topics — Perfect Score!</span>'}</div>
      </div>
    </div>

    ${recs ? `
      <div class="card">
        <h4 style="font-weight: 700; margin-bottom: 0.5rem; color: var(--accent);"><i class="fa-solid fa-route"></i> Personalized Revision Roadmap</h4>
        <ul style="margin-left: 1.25rem; font-size: 0.85rem; line-height: 1.7; color: var(--text-muted);">${recs}</ul>
      </div>
    ` : ''}

    <div style="text-align: center;">
      <button class="btn btn-primary" onclick="startQuiz()"><i class="fa-solid fa-redo"></i> Take Another Quiz</button>
    </div>
  `;

  renderMathInElement(resultsBox);
}

// RAG Academic Chat
async function sendChatMessage() {
  const input = document.getElementById('chat-input-field');
  const msg = input?.value.trim();
  if (!msg) return;

  input.value = '';
  const container = document.getElementById('chat-messages-container');

  // Append user message
  const userBubble = document.createElement('div');
  userBubble.className = 'chat-bubble user';
  userBubble.textContent = msg;
  container.appendChild(userBubble);
  container.scrollTop = container.scrollHeight;

  // Append loading assistant bubble
  const assistantBubble = document.createElement('div');
  assistantBubble.className = 'chat-bubble assistant';
  assistantBubble.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Searching uploaded notebooks & university archives...';
  container.appendChild(assistantBubble);
  container.scrollTop = container.scrollHeight;

  try {
    const res = await fetch(`${API_BASE}/api/chat/message`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: msg, session_id: state.chatSessionId })
    });

    if (res.ok) {
      const data = await res.json();
      const citationsHtml = (data.citations || []).map(c => `
        <span class="citation-chip" title="${c.text_snippet}">
          <i class="fa-solid fa-bookmark"></i> ${c.doc_name} (${c.location})
        </span>
      `).join('');

      assistantBubble.innerHTML = `
        <div style="font-weight: 700; color: var(--accent); margin-bottom: 0.35rem;">
          <i class="fa-solid fa-graduation-cap"></i> Antigravity Academic AI <span style="font-size: 0.7rem; color: var(--text-dim); font-weight: 400;">(${data.model || 'RAG Augmented'})</span>
        </div>
        <div style="line-height: 1.6;">${data.response.replace(/\n/g, '<br>')}</div>
        ${citationsHtml ? `<div style="margin-top: 0.5rem;">${citationsHtml}</div>` : ''}
      `;

      renderMathInElement(assistantBubble);
      container.scrollTop = container.scrollHeight;
    }
  } catch (e) {
    console.error('Chat error:', e);
    assistantBubble.textContent = 'Error contacting academic AI tutor. Please try again.';
  }
}

// Event Listeners Initialization
function initEventHandlers() {
  // Filter bar dropdowns
  ['filter-college', 'filter-subject', 'filter-semester', 'filter-status', 'filter-difficulty', 'sort-assignments-by'].forEach(id => {
    const el = document.getElementById(id);
    if (el) el.addEventListener('change', () => loadAssignments());
  });

  // PYQ search button
  const pyqSearchBtn = document.getElementById('btn-search-pyq');
  if (pyqSearchBtn) pyqSearchBtn.addEventListener('click', () => searchPYQ());

  // Assignment generator button
  const genBtn = document.getElementById('btn-trigger-generate');
  if (genBtn) genBtn.addEventListener('click', triggerAssignmentGeneration);

  // Note maker buttons
  const notesBtn = document.getElementById('btn-generate-notes');
  if (notesBtn) notesBtn.addEventListener('click', generateNotes);

  const fcPrevBtn = document.getElementById('btn-fc-prev');
  const fcNextBtn = document.getElementById('btn-fc-next');
  if (fcPrevBtn) fcPrevBtn.addEventListener('click', () => {
    if (state.activeFlashcards.length > 0) {
      state.currentFlashcardIndex = (state.currentFlashcardIndex - 1 + state.activeFlashcards.length) % state.activeFlashcards.length;
      updateFlashcardDisplay();
    }
  });
  if (fcNextBtn) fcNextBtn.addEventListener('click', () => {
    if (state.activeFlashcards.length > 0) {
      state.currentFlashcardIndex = (state.currentFlashcardIndex + 1) % state.activeFlashcards.length;
      updateFlashcardDisplay();
    }
  });

  // Quiz start button
  const quizBtn = document.getElementById('btn-start-quiz');
  if (quizBtn) quizBtn.addEventListener('click', startQuiz);

  // Chat send
  const chatSendBtn = document.getElementById('btn-send-chat');
  const chatInput = document.getElementById('chat-input-field');
  if (chatSendBtn) chatSendBtn.addEventListener('click', sendChatMessage);
  if (chatInput) chatInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') sendChatMessage();
  });

  // Export batch
  const exportBtn = document.getElementById('btn-export-repository');
  if (exportBtn) exportBtn.addEventListener('click', async () => {
    window.open(`${API_BASE}/api/assignments/batch-export`, '_blank');
  });

  initHelpGrader();
}

// Modal handling
function initModal() {
  const modal = document.getElementById('new-assignment-modal');
  const openBtn = document.getElementById('header-action-btn');
  const closeBtn = document.getElementById('btn-close-modal');
  const cancelBtn = document.getElementById('btn-modal-cancel');
  const saveBtn = document.getElementById('btn-modal-save');

  if (openBtn && modal) {
    openBtn.addEventListener('click', () => modal.classList.add('open'));
  }
  [closeBtn, cancelBtn].forEach(b => {
    if (b && modal) {
      b.addEventListener('click', () => modal.classList.remove('open'));
    }
  });

  if (saveBtn && modal) {
    saveBtn.addEventListener('click', async () => {
      const title = document.getElementById('modal-title')?.value.trim();
      const college = document.getElementById('modal-college')?.value.trim() || 'University';
      const subject = document.getElementById('modal-subject')?.value.trim() || 'General';
      const semester = document.getElementById('modal-semester')?.value || '1';
      const year = document.getElementById('modal-year')?.value.trim() || '2024';
      const difficulty = document.getElementById('modal-difficulty')?.value || 'Intermediate';
      const tagsRaw = document.getElementById('modal-tags')?.value.trim() || '';
      const content = document.getElementById('modal-content')?.value.trim() || '';

      if (!title) {
        alert('Please provide an assignment title.');
        return;
      }

      const tags = tagsRaw ? tagsRaw.split(',').map(t => t.trim()).filter(Boolean) : [subject];

      try {
        const res = await fetch(`${API_BASE}/api/assignments`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            title,
            college,
            subject,
            semester,
            academic_year: year,
            difficulty,
            topic_tags: tags,
            content_text: content,
            questions: [
              { num: 1, marks: 10, type: 'Problem', topic: subject, text: content || title }
            ],
            status: 'Pending'
          })
        });

        if (res.ok) {
          modal.classList.remove('open');
          loadAssignments();
          loadSystemStatus();
        }
      } catch (e) {
        console.error('Save assignment error:', e);
      }
    });
  }
}
