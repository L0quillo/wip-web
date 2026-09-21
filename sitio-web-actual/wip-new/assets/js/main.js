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

  // 6. Preselect form options from URL parameters (?servicio= o ?equipo=)
  const servicioSelect = document.getElementById('servicio');
  if (servicioSelect) {
    const urlParams = new URLSearchParams(window.location.search);
    const paramVal = urlParams.get('servicio') || urlParams.get('equipo');
    if (paramVal) {
      const normalizedParam = paramVal.toLowerCase().replace(/[-_]/g, ' ');
      for (let i = 0; i < servicioSelect.options.length; i++) {
        const opt = servicioSelect.options[i];
        const optText = opt.text.toLowerCase();
        const optVal = opt.value.toLowerCase();
        if (optVal.includes(normalizedParam) || optText.includes(normalizedParam) || 
            (normalizedParam.includes('caldera') && optVal.includes('caldera')) ||
            (normalizedParam.includes('vapor') && (optVal.includes('vapor') || optVal.includes('caldera'))) ||
            (normalizedParam.includes('biomasa') && optVal.includes('biomasa')) ||
            (normalizedParam.includes('fluido') && optVal.includes('fluido')) ||
            (normalizedParam.includes('agua caliente') && optVal.includes('agua caliente')) ||
            (normalizedParam.includes('automatizacion') && optVal.includes('automatizacion')) ||
            (normalizedParam.includes('iot') && optVal.includes('iot')) ||
            (normalizedParam.includes('sensor') && optVal.includes('sensor')) ||
            (normalizedParam.includes('tablero') && optVal.includes('tablero'))) {
          servicioSelect.selectedIndex = i;
          break;
        }
      }
    }
  }

  // 7. Ambient Video Background Control
  const heroVideo = document.getElementById('heroVideo');
  const ambientToggleBtn = document.getElementById('ambientToggleBtn');

  if (ambientToggleBtn && heroVideo) {
    ambientToggleBtn.addEventListener('click', () => {
      if (heroVideo.paused) {
        heroVideo.play().then(() => {
          ambientToggleBtn.innerHTML = `
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 9v6m4-6v6m7-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
            <span>Render 3D Activo</span>
          `;
        }).catch(() => {});
      } else {
        heroVideo.pause();
        ambientToggleBtn.innerHTML = `
          <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
          <span>Pausar Render</span>
        `;
      }
    });
  }

  // 8. Robust Video Fallback Engine (Static Image on Error or Low-Bandwidth)
  function convertVideoToStaticImage(video) {
    if (!video || video.dataset.fallbackApplied) return;
    video.dataset.fallbackApplied = 'true';

    const posterSrc = video.getAttribute('poster');
    if (!posterSrc) return;

    const img = document.createElement('img');
    img.src = posterSrc;
    img.alt = video.getAttribute('aria-label') || video.getAttribute('title') || 'Equipo Industrial WIP';
    if (video.className) img.className = video.className;
    if (video.getAttribute('style')) img.style.cssText = video.getAttribute('style');

    if (!img.style.width) img.style.width = '100%';
    if (!img.style.height) img.style.height = '100%';
    if (!img.style.objectFit) img.style.objectFit = 'cover';
    if (!img.style.display) img.style.display = 'block';

    if (video.parentNode) {
      video.parentNode.replaceChild(img, video);
    }
  }

  // Check network speed & data-saver mode
  const connection = navigator.connection || navigator.mozConnection || navigator.webkitConnection;
  const isSlowConnection = connection && (connection.saveData === true || connection.effectiveType === 'slow-2g' || connection.effectiveType === '2g');

  const allVideos = document.querySelectorAll('video');

  if (isSlowConnection) {
    // Under very slow connections or Data-Saver, immediately swap all videos for high-performance static images
    allVideos.forEach(v => convertVideoToStaticImage(v));
  } else {
    // Attach error listeners to guarantee fallback if any video stream fails
    allVideos.forEach(video => {
      video.addEventListener('error', () => {
        convertVideoToStaticImage(video);
      }, true);

      const sources = video.querySelectorAll('source');
      sources.forEach(src => {
        src.addEventListener('error', () => {
          convertVideoToStaticImage(video);
        });
      });
    });

    // 9. Lazy Playback & Resource Management with IntersectionObserver
    if ('IntersectionObserver' in window) {
      const videoObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          const video = entry.target;
          if (entry.isIntersecting) {
            if (video.paused && video.getAttribute('autoplay') !== null) {
              const playPromise = video.play();
              if (playPromise !== undefined) {
                playPromise.catch(() => {
                  // If autoplay blocked (e.g. low power mode), poster remains visible naturally
                });
              }
            }
          } else {
            if (!video.paused) {
              video.pause();
            }
          }
        });
      }, { rootMargin: '80px 0px', threshold: 0.1 });

      allVideos.forEach(v => {
        if (v.getAttribute('autoplay') !== null) {
          videoObserver.observe(v);
        }
      });
    }
  }
});
