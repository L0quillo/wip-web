/**
 * WIP INDUSTRIAL - Master JavaScript
 * Interactivity, Filtering, Modals and Mobile Navigation
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Mobile Menu Toggle
  const mobileToggle = document.getElementById('mobileToggle');
  const mainNav = document.getElementById('mainNav');

  if (mobileToggle && mainNav) {
    mobileToggle.addEventListener('click', () => {
      mainNav.classList.toggle('active');
      const isExpanded = mainNav.classList.contains('active');
      mobileToggle.setAttribute('aria-expanded', isExpanded);
    });

    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
      if (!mainNav.contains(e.target) && !mobileToggle.contains(e.target) && mainNav.classList.contains('active')) {
        mainNav.classList.remove('active');
        mobileToggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // 2. Sticky Header Effect
  const header = document.querySelector('.site-header');
  if (header) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 20) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    }, { passive: true });
  }

  // 3. Tab Filter System
  const filterBtns = document.querySelectorAll('.tab-btn[data-filter]');
  const filterItems = document.querySelectorAll('.filterable-item');

  if (filterBtns.length > 0 && filterItems.length > 0) {
    filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const filter = btn.getAttribute('data-filter');

        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        filterItems.forEach(item => {
          const category = item.getAttribute('data-category');
          if (filter === 'all' || category === filter || (category && category.includes(filter))) {
            item.style.display = '';
            item.style.opacity = '0';
            setTimeout(() => {
              item.style.transition = 'opacity 0.3s ease';
              item.style.opacity = '1';
            }, 20);
          } else {
            item.style.display = 'none';
          }
        });
      });
    });
  }

  // 4. Modal / Ficha Técnica Viewer
  const modal = document.getElementById('techModal');
  const modalTitle = document.getElementById('modalTitle');
  const modalCategory = document.getElementById('modalCategory');
  const modalBody = document.getElementById('modalBodyContent');
  const modalClose = document.getElementById('modalClose');
  const openModalBtns = document.querySelectorAll('[data-open-modal]');

  function openTechModal(title, category, contentHtml) {
    if (!modal) return;
    if (modalTitle) modalTitle.textContent = title;
    if (modalCategory) modalCategory.textContent = category;
    if (modalBody) modalBody.innerHTML = contentHtml;
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeTechModal() {
    if (!modal) return;
    modal.classList.remove('active');
    document.body.style.overflow = '';
  }

  if (openModalBtns.length > 0 && modal) {
    openModalBtns.forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        const targetId = btn.getAttribute('data-open-modal');
        const dataElement = document.getElementById(targetId);
        if (dataElement) {
          const title = dataElement.getAttribute('data-title') || 'Especificación Técnica';
          const category = dataElement.getAttribute('data-category') || 'WIP Industrial';
          const content = dataElement.innerHTML;
          openTechModal(title, category, content);
        }
      });
    });
  }

  if (modalClose) {
    modalClose.addEventListener('click', closeTechModal);
  }

  if (modal) {
    modal.addEventListener('click', (e) => {
      if (e.target === modal) {
        closeTechModal();
      }
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && modal.classList.contains('active')) {
        closeTechModal();
      }
    });
  }

  // 5. Contact Form Handler (Async AJAX with PHP fallback)
  const contactForm = document.getElementById('wipContactForm');
  const formStatus = document.getElementById('formStatus');

  if (contactForm && formStatus) {
    contactForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const submitBtn = contactForm.querySelector('button[type="submit"]');
      const originalBtnText = submitBtn ? submitBtn.innerHTML : 'Enviar';

      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerHTML = 'Enviando requerimiento...';
      }

      formStatus.style.display = 'none';
      formStatus.className = 'form-status';

      const formData = new FormData(contactForm);

      try {
        const response = await fetch('send-contact.php', {
          method: 'POST',
          body: formData
        });

        const result = await response.json();

        if (result.success) {
          formStatus.textContent = result.message || 'Mensaje enviado exitosamente. Un ingeniero de WIP se pondrá en contacto a la brevedad.';
          formStatus.classList.add('success');
          contactForm.reset();
        } else {
          formStatus.textContent = result.message || 'Hubo un error al procesar el mensaje. Por favor contáctenos directamente por WhatsApp o teléfono.';
          formStatus.classList.add('error');
        }
      } catch (err) {
        // Fallback info
        formStatus.textContent = 'Gracias por contactar a WIP. Su solicitud ha sido registrada o puede comunicarse inmediatamente por WhatsApp.';
        formStatus.classList.add('success');
      } finally {
        formStatus.style.display = 'block';
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.innerHTML = originalBtnText;
        }
      }
    });
  }
});
