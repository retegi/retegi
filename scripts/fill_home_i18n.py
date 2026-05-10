#!/usr/bin/env python3
"""
Fill translations for homepage / base navbar / RetegiBot strings in django.po files.
Run from project root: python scripts/fill_home_i18n.py
Or: docker compose exec web python scripts/fill_home_i18n.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import polib

ROOT = Path(__file__).resolve().parents[1]
LOCALE_DIR = ROOT / "locale"


def ctxt_key(entry: polib.POEntry) -> tuple[str, str]:
    return (entry.msgctxt or "", entry.msgid)


_DAY_DJANGO = (
    "Day to day it\u2019s Django and Python deployed for real workloads: "
    "containers, owned servers and maintainable operations. AI only when it "
    "really helps (RAG, assistants and automation of grunt work); side projects "
    "vet ideas before they ever reach collaborators."
)

_SPANISH: dict[tuple[str, str], str] = {
    ("", "Euskara"): "Euskara",
    ("", "Castellano"): "Castellano",
    ("", "English"): "Inglés",
    ("", "Contact"): "Contacto",
    ("", "Retegi"): "Retegi",
    ("", "retegi.eus"): "retegi.eus",
    ("", "Main menu"): "Menú principal",
    ("", "Projects"): "Proyectos",
    ("", "Services"): "Servicios",
    ("", "Lab"): "Laboratorio",
    ("", "Blog"): "Blog",
    ("", "Choose language"): "Elegir idioma",
    ("", "Let's talk"): "Hablemos",
    (
        "",
        "Tell me briefly what you need and I'll get back to you.",
    ): (
        "Cuéntame brevemente qué necesitas y te responderé."
    ),
    ("", "Message sent"): "Mensaje enviado",
    ("", "Thank you"): "Gracias",
    (
        "",
        "Your message has been sent. I'll reply as soon as I can.",
    ): ("Tu mensaje se ha enviado. Contestaré lo antes posible."),
    ("", "Back to home"): "Volver al inicio",
    ("", "Send another message"): "Enviar otro mensaje",
    (
        "",
        "Your message has been sent successfully. I'll reply as soon as I can.",
    ): (
        "Mensaje enviado correctamente. Te responderé lo antes posible."
    ),
    (
        "",
        "We could not send your message. Please try again later.",
    ): (
        "No se ha podido enviar el mensaje. Inténtalo de nuevo más tarde."
    ),
    (
        "",
        "Useful web software, automation and AI solutions. Real projects, your own "
        "infra, and a practical approach for teams that want to ship fast without losing control.",
    ): (
        "Software web útil, automatización e IA. Proyectos reales, tu propia infraestructura "
        "y un enfoque práctico para equipos que quieren entregar rápido sin perder el control."
    ),
    ("", "AI &amp; RAG"): "IA y RAG",
    ("", "Navigation"): "Navegación",
    ("", "Legal &amp; extras"): "Legal y extras",
    ("", "Privacy"): "Privacidad",
    ("", "Cookies"): "Cookies",
    ("", "Legal"): "Aviso legal",
    ("", "Ideas or collaborations? Message me via the form."): (
        "¿Ideas o colaboraciones? Escríbeme desde el formulario."
    ),
    ("", "Go to contact →"): "Ir a contacto →",
    ("", "Social profiles"): "Perfiles sociales",
    ("", "GitHub — coming soon"): "GitHub — próximamente",
    ("", "LinkedIn — coming soon"): "LinkedIn — próximamente",
    ("", "Made with Django and lots of ☕."): "Hecho con Django y mucho ☕.",
    ("", "RetegiBot"): "RetegiBot",
    ("", "Assistant · retegi.eus"): "Asistente · retegi.eus",
    ("", "Close RetegiBot"): "Cerrar RetegiBot",
    (
        "",
        "Kaixo, I'm RetegiBot. I can help you with web projects, automation, AI or servers.",
    ): (
        "Kaixo, soy RetegiBot. Puedo ayudarte con proyectos web, automatizaciones, IA o "
        "servidores."
    ),
    ("", "Your message"): "Tu mensaje",
    ("", "Type your question…"): "Escribe tu consulta...",
    ("", "Open RetegiBot"): "Abrir RetegiBot",
    ("", "Contact me"): "Contactar",
    ("", "Retegi · retegi.eus — Web development, automation & AI"): (
        "Retegi · retegi.eus — Desarrollo web, automatización e IA"
    ),
    (
        "",
        "Useful web software, automation and AI for real-world projects — Django servers, Docker, and tools that save time.",
    ): (
        "Software útil, automatización e IA para proyectos reales: servidores Django, "
        "Docker y herramientas que ahorran tiempo."
    ),
    ("", "Retegi · retegi.eus"): "Retegi · retegi.eus",
    (
        "",
        "Web development, apps and digital solutions with modern technologies.",
    ): (
        "Desarrollo web, apps y soluciones digitales con tecnologías actuales."
    ),
    (
        "",
        "I create custom digital tools for businesses, projects and professionals: modern websites, internal applications, automations, AI assistants and connected systems.",
    ): (
        "Creo herramientas digitales a medida para empresas, proyectos y profesionales: "
        "webs modernas, aplicaciones internas, automatizaciones, asistentes IA y sistemas conectados."
    ),
    ("", "View projects"): "Ver proyectos",
    ("", "Talk about an idea"): "Hablar de una idea",
    ("", "Django · Python"): "Django · Python",
    ("", "Web apps"): "Apps web",
    ("", "Artificial intelligence"): "Inteligencia artificial",
    ("", "Robotics"): "Robótica",
    ("", "Docker & Linux"): "Docker y Linux",
    ("", "RAG · assistants"): "RAG · asistentes",
    (
        "",
        "Retegi — software, automation and artificial intelligence",
    ): (
        "Retegi — software, automatización e inteligencia artificial"
    ),
    (
        "",
        "Retegi — software developer, automation and artificial intelligence",
    ): (
        "Retegi — desarrollador de software, automatización e inteligencia artificial"
    ),
    ("", "~/projects"): "~/proyectos",
    ("terminal-status", "OK"): "OK",
    ("", "deploy ready"): "listo para desplegar",
    ("terminal-line", "docker compose ps"): "docker compose ps",
    ("terminal-line", "web · online"): "web · en línea",
    ("infra-badge", "local"): "local",
    ("", "REST API"): "API REST",
    ("", "CI · scripts"): "CI · scripts",
    ("", "TLS · nginx"): "TLS · nginx",
    ("", "REST"): "REST",
    ("", "CI"): "CI",
    ("heading", "Intro"): "Intro",
    (
        "",
        "I develop web software, applications and AI-assisted solutions with a practical mindset.",
    ): (
        "Desarrollo software web, aplicaciones y soluciones con IA aplicada, "
        "con mentalidad práctica."
    ),
    ("", _DAY_DJANGO): (
        "El día a día es Django y Python desplegados para cargas reales: contenedores, "
        "servidores propios y operaciones mantenibles. IA solo cuando aporta de verdad "
        "(RAG, asistentes y automatización del trabajo pesado); los proyectos laterales "
        "validan ideas antes de llegar a colaboradores."
    ),
    (
        "",
        "Clean code, incremental delivery and someone who respects both engineers and stakeholders — that combination usually clicks.",
    ): (
        "Código limpio, entrega incremental y alguien que respeta a ingenierías y negocio; "
        "esa combinación suele funcionar."
    ),
    ("", "Daily stack"): "Stack diario",
    ("", "The process"): "El proceso",
    ("", "A clear, close way of working with clients"): (
        "Una forma clara y cercana de trabajar con el cliente"
    ),
    (
        "",
        "From idea to a useful tool: listen, understand, design, develop and improve.",
    ): (
        "De la idea a una herramienta útil: escuchar, entender, diseñar, desarrollar y "
        "mejorar."
    ),
    (
        "",
        "Comic explaining how we collaborate with clients",
    ): "Viñetas que explican el proceso de trabajo con el cliente",
    ("", "Python · Django · Bootstrap"): "Python · Django · Bootstrap",
    ("", "Docker · nginx · Gunicorn"): "Docker · nginx · Gunicorn",
    ("", "PostgreSQL · SQLite"): "PostgreSQL · SQLite",
    ("", "AI · RAG · embeddings"): "IA · RAG · embeddings",
    ("", "Automation (scripts, pipelines)"): "Automatización (scripts, pipelines)",
    ("", "Linux servers · backups · TLS"): "Servidores Linux · copias de seguridad · TLS",
    ("technologies", "Referenced in posts"): "Mencionado en los artículos",
    ("", "What I do"): "Qué hago",
    ("", "From idea to stable service in production."): (
        "De la idea al servicio estable en producción."
    ),
    (
        "",
        "No corporate fluff: deliverables you can actually run, observe and iterate when it's time to scale.",
    ): (
        "Sin relleno corporativo: entregables que puedes ejecutar, observar e iterar "
        "cuando toque escalar."
    ),
    ("", "Web development"): "Desarrollo web",
    (
        "",
        "Responsive sites and Django apps engineered for readability, uptime and sane releases.",
    ): (
        "Sitios responsivos y apps Django pensadas para legibilidad, disponibilidad "
        "y releases sensatas."
    ),
    ("", "Custom software"): "Software a medida",
    (
        "",
        "Back-office dashboards, invoicing stacks, bookings, terminals and workflows tailored to messy reality.",
    ): (
        "Cuadros de mando internos, facturación, reservas, terminales y flujos de trabajo "
        "adaptados a la realidad caótica."
    ),
    ("", "AI & automation"): "IA y automatización",
    (
        "",
        "Assistants grounded on your corpus, ingestion pipelines and automation that survives Monday mornings.",
    ): (
        "Asistentes anclados a tu corpus, tuberías de ingesta y automatización "
        "que aguantan los lunes por la mañana."
    ),
    ("", "Servers & deployments"): "Servidores y despliegues",
    (
        "",
        "Docker, nginx, Gunicorn, hardened Linux hosts, HTTPS, snapshots and repeatable deploys.",
    ): (
        "Docker, nginx, Gunicorn, hosts Linux endurecidos, HTTPS, instantáneas "
        "y despliegues repetibles."
    ),
    ("", "Highlights"): "Destacados",
    ("", "Featured projects"): "Proyectos destacados",
    ("", "Official URLs arriving soon wherever noted."): (
        "Las URLs oficiales llegarán pronto donde se indique."
    ),
    (
        "",
        "Exam prep cockpit with bilingual assets, granular progress and thoughtful PRO tiers.",
    ): (
        "Cockpit de preparación de exámenes con recursos bilingües, progreso granular "
        "y niveles PRO bien pensados."
    ),
    ("", "AI"): "IA",
    ("", "View project"): "Ver proyecto",
    (
        "",
        "Transparency layer for comparing public sector platforms with curated rankings plus an IA/RAG copilot.",
    ): (
        "Capa de transparencia para comparar plataformas del sector público con rankings "
        "curados y un copiloto IA/RAG."
    ),
    ("", "RAG"): "RAG",
    ("", "Learn more"): "Saber más",
    (
        "",
        "Experiments marrying geodata, humane interfaces and pragmatic AI-assisted workflows.",
    ): (
        "Experimentos que unen datos geográficos, interfaces humanas y flujos asistidos por IA pragmática."
    ),
    ("badge", "maps"): "mapas",
    ("", "Explore"): "Explorar",
    ("", "Ares · local IA"): "Ares · IA local",
    (
        "",
        "Hands-free assistant leaning on local Ollama models, scripted homes and pragmatic privacy posture.",
    ): (
        "Asistente manos libres basado en modelos locales Ollama, hogares con scripts "
        "y una postura de privacidad pragmática."
    ),
    ("hardware", "Voice"): "Voz",
    ("", "Details"): "Detalles",
    (
        "",
        "Creative outlet mixing playful culture geekery with serious shipping discipline behind the curtain.",
    ): (
        "Válvula creativa entre frikismo cultural y disciplina seria de producción "
        "tras el telón."
    ),
    (
        "",
        "Hybrid POS orchestration bridging stock, cashier UX and bookkeeping without brittle spreadsheets.",
    ): (
        "Orquestación híbrida de TPV entre stock, experiencia en caja y contabilidad "
        "sin hojas frágiles."
    ),
    ("", "Retail ops"): "Retail",
    ("", "Playground"): "Zona experimental",
    ("", "Retegi Lab"): "Laboratorio Retegi",
    (
        "",
        "Hands-on tinkering bench: autonomous agents, tactile robots, choropleths, scraped-but-respectful pipelines and pragmatic analytics you can rerun next week with coffee in hand.",
    ): (
        "Banco práctico: agentes autónomos, robots táctiles, coropletas, scraping respetuoso "
        "y analítica pragmática que puedes repetir la semana que viene con un café en la mano."
    ),
    ("", "Local assistants"): "Asistentes locales",
    (
        "",
        "Tiny models glued to notebooks, scripted wake words and repeatable evaluation harnesses.",
    ): (
        "Modelos pequeños enlazados a notebooks, palabras de activación por script "
        "y suites de evaluación repetibles."
    ),
    ("", "Maps · data viz"): "Mapas · visualización de datos",
    (
        "",
        "Composable layers, ingestion scripts and humane defaults for exploratory storytelling.",
    ): (
        "Capas componibles, scripts de ingesta y valores por defecto humanos "
        "para narrativa exploratoria."
    ),
    ("", "Robotics / Raspberry Pi prototypes"): "Robótica / prototipos Raspberry Pi",
    (
        "",
        "Breadboard bravery: GPIO experiments, kiosk boards and reproducible BOM notes.",
    ): (
        "Valor en protoboard: experimentos GPIO, kioskos y listas de materiales reproducibles."
    ),
    ("", "Technical blog"): "Blog técnico",
    ("", "Back to top"): "Volver arriba",
    ("", "Read article →"): "Leer artículo →",
    ("", "Deploy"): "Despliegue",
    ("", "Shipping Django behind Docker, Gunicorn & nginx"): (
        "Publicar Django con Docker, Gunicorn y nginx"
    ),
    (
        "",
        "Operational checklist from zero-ish to TLS with backups you can swear by.",
    ): (
        "Lista operativa desde casi cero hasta TLS con copias en las que confiar."
    ),
    ("", "Continue reading →"): "Seguir leyendo →",
    ("", "Local IA"): "IA local",
    (
        "",
        "Responsible local AI workflows you can iterate on nightly",
    ): "Flujos responsables de IA local que puedes iterar cada noche",
    (
        "",
        "Thinking through when modest models outperform giant APIs without leaking payloads.",
    ): "Cuándo modelos modestos superan APIs gigantes sin filtrar datos sensibles.",
    ("", "Productivity"): "Productividad",
    (
        "",
        "Automating small chores that secretly eat half your roadmap",
    ): (
        "Automatizar las tareas pequeñas que se meriendan la mitad de tu roadmap en silencio"
    ),
    (
        "",
        "Email triage helpers, politely scoped scrapers and sleepy cronfriends that amortize infra.",
    ): (
        "Asistentes de correo, scrapers bien acotados y crons amortiguadores de infraestructura."
    ),
    ("cta", "Next beat"): "Siguiente paso",
    ("", "Do you have an idea or a process you want to improve?"): (
        "¿Tienes una idea o un proceso que quieres mejorar?"
    ),
    (
        "",
        "I can translate it into a web tool, automate the boring limbs or scaffold the whole dependable system.",
    ): (
        "Puedo traducirlo a una herramienta web, automatizar lo aburrido "
        "o montar el sistema fiable de punta a punta."
    ),
    ("", "Digital manifesto"): "MANIFIESTO DIGITAL",
    (
        "",
        "Values for ethical, sustainable and human technology.",
    ): "Valores para una tecnología ética, sostenible y humana.",
    (
        "",
        "A digital community is not only defined by the tools it uses, but by the principles with which it builds, shares and maintains them.",
    ): (
        "Una comunidad digital no solo se define por las herramientas que usa, sino por "
        "los principios con los que las construye, comparte y mantiene."
    ),
    ("", "Retegi digital values"): "Valores digitales de Retegi",
    ("", "ethics"): "ética",
    ("", "data"): "datos",
    ("", "human"): "humano",
    ("", "open"): "abierto",
    ("", "Ethical artificial intelligence"): "Inteligencia artificial ética",
    ("", "Digital sovereignty"): "Soberanía digital",
    ("", "Privacy by design"): "Privacidad por diseño",
    ("", "Sustainable technology"): "Tecnología sostenible",
    ("", "Useful and human software"): "Software útil y humano",
    ("", "Universal accessibility"): "Accesibilidad universal",
    ("", "Algorithmic transparency"): "Transparencia algorítmica",
    ("", "Meaningful human control"): "Control humano significativo",
    ("", "Open and collaborative culture"): "Cultura abierta y colaborativa",
    ("", "Responsible security"): "Seguridad responsable",
    ("", "Linguistic and cultural inclusion"): "Inclusión lingüística y cultural",
    ("", "Independence from digital monopolies"): "Independencia frente a monopolios digitales",
    ("", "Critical digital literacy"): "Alfabetización digital crítica",
    ("", "Data for the common good"): "Datos al servicio del bien común",
    ("", "Technological minimalism"): "Minimalismo tecnológico",
    ("", "Interoperability"): "Interoperabilidad",
    ("", "Repairability and maintenance"): "Reparabilidad y mantenimiento",
    ("", "Smart decentralization"): "Descentralización inteligente",
    ("", "Digital wellbeing"): "Bienestar digital",
    ("", "Technological social responsibility"): "Responsabilidad social tecnológica",
    ("", "Retegi system"): "Sistema Retegi",
    ("", "online"): "online",
    ("", "django-admin startproject"): "django-admin startproject",
    ("", "docker compose up -d"): "docker compose up -d",
    ("", "python manage.py deploy"): "python manage.py deploy",
    ("", "API REST online"): "API REST online",
    ("", "RAG assistant ready"): "Asistente RAG listo",
    ("", "SSL + Nginx active"): "SSL + Nginx activo",
    ("", "AI local"): "IA local",
    ("", "Automation"): "Automatización",
    ("", "Django"): "Django",
    ("", "Docker"): "Docker",
    ("", "Nginx"): "Nginx",
    ("", "You:"): "Tú:",
    ("", "Bot:"): "Bot:",
    ("", "Something went wrong."): "Algo salió mal.",
    ("", "Could not reach the server."): "No se pudo conectar con el servidor.",
}

_BASELINE: dict[tuple[str, str], str] = {
    ("", "Euskara"): "Euskara",
    ("", "Castellano"): "Gaztelania",
    ("", "English"): "Ingelesera",
    ("", "Contact"): "Kontaktua",
    ("", "Retegi"): "Retegi",
    ("", "retegi.eus"): "retegi.eus",
    ("", "Main menu"): "Menu nagusia",
    ("", "Projects"): "Proiektuak",
    ("", "Services"): "Zerbitzuak",
    ("", "Lab"): "Laborategia",
    ("", "Blog"): "Bloga",
    ("", "Choose language"): "Hautatu hizkuntza",
    ("", "Let's talk"): "Hitz egin",
    (
        "",
        "Tell me briefly what you need and I'll get back to you.",
    ): (
        "Esadazu labur zer behar duzun eta hobeto erantzungo dizut."
    ),
    ("", "Message sent"): "Mezua bidalita",
    ("", "Thank you"): "Eskerrik asko",
    (
        "",
        "Your message has been sent. I'll reply as soon as I can.",
    ): (
        "Mezua bidali duzu. Ahal bezain laster erantzungo dizut."
    ),
    ("", "Back to home"): "Itzuli hasierara",
    ("", "Send another message"): "Beste mezu bat bidali",
    (
        "",
        "Your message has been sent successfully. I'll reply as soon as I can.",
    ): (
        "Ongi bidali da mezua. Ahal bezain laster erantzungo dizut."
    ),
    (
        "",
        "We could not send your message. Please try again later.",
    ): (
        "Ezin izan da mezua bidali. Saiatu berriro beranduago."
    ),
    (
        "",
        "Useful web software, automation and AI solutions. Real projects, your own infra, and a practical approach for teams that want to ship fast without losing control.",
    ): (
        "Software web erabilgarria, automatizazioa eta IA soluzioak. Proiektu errealak, "
        "zure infraestructura eta talde azkar entregatu nahi dutenak kontrol galdu "
        "gabe eusteko ikuspegia."
    ),
    ("", "AI &amp; RAG"): "IA eta RAG",
    ("", "Navigation"): "Nabigazioa",
    ("", "Legal &amp; extras"): "Lege arlokoak eta gehigarriak",
    ("", "Privacy"): "Pribatutasuna",
    ("", "Cookies"): "Cookieak",
    ("", "Legal"): "Lege-oharra",
    ("", "Ideas or collaborations? Message me via the form."): (
        "Ideia edo lankidetzarik? Jarri zaitez nirekin harremanetan formularioaren bidez."
    ),
    ("", "Go to contact →"): "Joan kontaktura →",
    ("", "Social profiles"): "Sare sozialen profilak",
    ("", "GitHub — coming soon"): "GitHub — laster",
    ("", "LinkedIn — coming soon"): "LinkedIn — laster",
    ("", "Made with Django and lots of ☕."): "Djangorekin eta ☕ askorekin egina.",
    ("", "RetegiBot"): "RetegiBot",
    ("", "Assistant · retegi.eus"): "Laguntzailea · retegi.eus",
    ("", "Close RetegiBot"): "Itxi RetegiBot",
    (
        "",
        "Kaixo, I'm RetegiBot. I can help you with web projects, automation, AI or servers.",
    ): (
        "Kaixo, RetegiBot naiz. Web proiektuetan, automatizazioetan, IA edo "
        "zerbitzarietan lagundu diezazuket."
    ),
    ("", "Your message"): "Zure mezua",
    ("", "Type your question…"): "Idatzi zure kontsulta...",
    ("", "Open RetegiBot"): "Ireki RetegiBot",
    ("", "Contact me"): "Jarri harremanetan",
    ("", "Retegi · retegi.eus — Web development, automation & AI"): (
        "Retegi · retegi.eus — Web garapena, automatizazioa eta IA"
    ),
    (
        "",
        "Useful web software, automation and AI for real-world projects — Django servers, Docker, and tools that save time.",
    ): (
        "Software erabilgarria, automatizazioa eta IA proiektu errealentzat "
        "— Django zerbitzariak, Docker eta denbora aurrezteko tresnak."
    ),
    ("", "Retegi · retegi.eus"): "Retegi · retegi.eus",
    (
        "",
        "Web development, apps and digital solutions with modern technologies.",
    ): "Web garapena, app-ak eta soluzio digitalak teknologia berriekin.",
    (
        "",
        "I create custom digital tools for businesses, projects and professionals: modern websites, internal applications, automations, AI assistants and connected systems.",
    ): (
        "Enpresa, proiektu eta profesionalentzako tresna digitalak neurrira sortzen ditut: "
        "web modernoagoak, barne-aplikazioak, automatizazioak, IA laguntzaileak eta sistema "
        "konektatuak."
    ),
    ("", "View projects"): "Ikusi proiektuak",
    ("", "Talk about an idea"): "Ideia batez hitz egin",
    ("", "Django · Python"): "Django · Python",
    ("", "Web apps"): "Web app-ak",
    ("", "Artificial intelligence"): "Adimen artifiziala",
    ("", "Robotics"): "Robotika",
    ("", "Docker & Linux"): "Docker eta Linux",
    ("", "RAG · assistants"): "RAG · laguntzaileak",
    (
        "",
        "Retegi — software, automation and artificial intelligence",
    ): ("Retegi - softwarea, automatizazioa eta adimen artifiziala"),
    (
        "",
        "Retegi — software developer, automation and artificial intelligence",
    ): (
        "Retegi — software garatzailea, automatizazioa eta adimen artifiziala"
    ),
    ("", "~/projects"): "~/proiektuak",
    ("terminal-status", "OK"): "OK",
    ("", "deploy ready"): "hedapenerako prest",
    ("terminal-line", "docker compose ps"): "docker compose ps",
    ("terminal-line", "web · online"): "web · sarean",
    ("infra-badge", "local"): "lokala",
    ("", "REST API"): "REST API",
    ("", "CI · scripts"): "CI · script-ak",
    ("", "TLS · nginx"): "TLS · nginx",
    ("", "REST"): "REST",
    ("", "CI"): "CI",
    ("heading", "Intro"): "Sarrera",
    (
        "",
        "I develop web software, applications and AI-assisted solutions with a practical mindset.",
    ): (
        "Software web, aplikazio eta IA lagundutako soluzioak garatzen ditut, ikuspegi "
        "praktikoarekin."
    ),
    ("", _DAY_DJANGO): (
        "Egunerokoa Django eta Python lan errealengarako da: kontenedoreak, jabetzako "
        "zerbitzariak eta mantentzeko eragiketa arrazionalak. IA benetan laguntzen duenean "
        "soilik (RAG, laguntzaileak eta lan astunaren automatizazioa); proiektu pertsonalek "
        "balioztatu egiten dituzte ideiak lankidetza bidean sartu aurretik."
    ),
    (
        "",
        "Clean code, incremental delivery and someone who respects both engineers and stakeholders — that combination usually clicks.",
    ): (
        "Kode garbia, entrega inkrementala eta ingeniariak eta interes-taldeak "
        "errespetatzen dituen norbait — konbinazio horrek askotan jotzen du nahikoa."
    ),
    ("", "Daily stack"): "Eguneroko stack-a",
    ("", "The process"): "Prozesua",
    ("", "A clear, close way of working with clients"): (
        "Bezeroarekin lan egiteko modu argia eta gertukoa"
    ),
    (
        "",
        "From idea to a useful tool: listen, understand, design, develop and improve.",
    ): (
        "Ideiatik tresna erabilgarrira: entzun, ulertu, diseinatu, garatu eta hobetu."
    ),
    (
        "",
        "Comic explaining how we collaborate with clients",
    ): "Bezeroarekin lan egiteko prozesua azaltzen duen komikia",
    ("", "Python · Django · Bootstrap"): "Python · Django · Bootstrap",
    ("", "Docker · nginx · Gunicorn"): "Docker · nginx · Gunicorn",
    ("", "PostgreSQL · SQLite"): "PostgreSQL · SQLite",
    ("", "AI · RAG · embeddings"): "IA · RAG · embedding-ak",
    ("", "Automation (scripts, pipelines)"): "Automatizazioa (script-ak, pipeline-ak)",
    ("", "Linux servers · backups · TLS"): "Linux zerbitzariak · babeskopiak · TLS",
    ("technologies", "Referenced in posts"): "Artikuluetan aipatuta",
    ("", "What I do"): "Zer egiten dut",
    ("", "From idea to stable service in production."): (
        "Ideiatik produkzioko zerbitzu egonkor batera."
    ),
    (
        "",
        "No corporate fluff: deliverables you can actually run, observe and iterate when it's time to scale.",
    ): (
        "Korporazio-txantxarik gabe: exekuta, behatu eta eskalatu behar "
        "duzunean iteratu ditzakezun entregagarriak."
    ),
    ("", "Web development"): "Web garapena",
    (
        "",
        "Responsive sites and Django apps engineered for readability, uptime and sane releases.",
    ): (
        "Gune erantzunkorrak eta irakurgarritasunerako, uptime-rako eta jarraibide "
        "arrazionalak dituzten Django aplikazioak."
    ),
    ("", "Custom software"): "Neurrirako softwarea",
    (
        "",
        "Back-office dashboards, invoicing stacks, bookings, terminals and workflows tailored to messy reality.",
    ): (
        "Barne arbelak, fakturazioa, erreserbak, terminalak eta benetako "
        "kaosara egokitzen diren fluxuak."
    ),
    ("", "AI & automation"): "IA eta automatizazioa",
    (
        "",
        "Assistants grounded on your corpus, ingestion pipelines and automation that survives Monday mornings.",
    ): (
        "Zure corpusean oinarritutako laguntzaileak, ingestion pipeline-ak eta astelehen "
        "goizetan irauten duen automatizazioa."
    ),
    ("", "Servers & deployments"): "Zerbitzariak eta hedapenak",
    (
        "",
        "Docker, nginx, Gunicorn, hardened Linux hosts, HTTPS, snapshots and repeatable deploys.",
    ): (
        "Docker, nginx, Gunicorn, Linux zerbitzari sendotuak, HTTPS, berehalako "
        "argazkiak eta errepikatzen diren hedapenak."
    ),
    ("", "Highlights"): "Nabarmengarriak",
    ("", "Featured projects"): "Proiektu nabarmenak",
    ("", "Official URLs arriving soon wherever noted."): (
        "URL ofizialak laster helduko dira adierazi den tokietan."
    ),
    (
        "",
        "Exam prep cockpit with bilingual assets, granular progress and thoughtful PRO tiers.",
    ): (
        "Azterketa-ingurunea buru-bihurriekin: baliabide elebidunak, aurrera mailakakoa eta PRO "
        "mailen diseinu arretazkoa."
    ),
    ("", "AI"): "IA",
    ("", "View project"): "Ikusi proiektua",
    (
        "",
        "Transparency layer for comparing public sector platforms with curated rankings plus an IA/RAG copilot.",
    ): (
        "Sektore publikoaren plataformak zerrendatuak alderatzeko gardentasun-geruza "
        "+ IA/RAG kopilotoa."
    ),
    ("", "RAG"): "RAG",
    ("", "Learn more"): "Gehiago jakiteko",
    (
        "",
        "Experiments marrying geodata, humane interfaces and pragmatic AI-assisted workflows.",
    ): (
        "Geo-datuak, interfaze erabilerrazak eta IA lagundutako fluxu pragmatikoak nahasten "
        "dituzten esperimentuak."
    ),
    ("badge", "maps"): "mapak",
    ("", "Explore"): "Arakatu",
    ("", "Ares · local IA"): "Ares · IA lokala",
    (
        "",
        "Hands-free assistant leaning on local Ollama models, scripted homes and pragmatic privacy posture.",
    ): (
        "Ollama modeloez oinarritutako esku-gabeko laguntzailea, script-etxeak eta "
        "ikuspegi pragmatiko pribatura."
    ),
    ("hardware", "Voice"): "Ahotsa",
    ("", "Details"): "Xehetasunak",
    (
        "",
        "Creative outlet mixing playful culture geekery with serious shipping discipline behind the curtain.",
    ): (
        "Kultura-frikismo jostalariaren eta cortinaren atzealdeko diziplina sendoaren konbinazioa."
    ),
    (
        "",
        "Hybrid POS orchestration bridging stock, cashier UX and bookkeeping without brittle spreadsheets.",
    ): (
        "POS hibridoaren orkestra: stock-a, kutxako UXa eta kontabilitatea, "
        "hautsitzen diren excelik gabe."
    ),
    ("", "Retail ops"): "Salmenta eragiketak",
    ("", "Playground"): "Jolaslekua",
    ("", "Retegi Lab"): "Retegi Laborategia",
    (
        "",
        "Hands-on tinkering bench: autonomous agents, tactile robots, choropleths, scraped-but-respectful pipelines and pragmatic analytics you can rerun next week with coffee in hand.",
    ): (
        "Eskuko tailerra: agente autonomoak, robota ukituak, koropletak, errespetuzko "
        "scraping fluxuak eta analitika pragmatikoa hurrengo astean kafe bat eskutan "
        "berrepikatzen dena."
    ),
    ("", "Local assistants"): "Laguntzaile lokalak",
    (
        "",
        "Tiny models glued to notebooks, scripted wake words and repeatable evaluation harnesses.",
    ): (
        "Modelo txikiak koadernoetan erantsita, wake-word scriptatuak eta ebaluazio "
        "errepikagarrietarako sareak."
    ),
    ("", "Maps · data viz"): "Mapak · bisualizazioa",
    (
        "",
        "Composable layers, ingestion scripts and humane defaults for exploratory storytelling.",
    ): (
        "Geruza konposagarriak, ingestion script-ak eta historia arakarako lehenespenezko "
        "balio humanoak."
    ),
    ("", "Robotics / Raspberry Pi prototypes"): "Robotika / Raspberry Pi prototipoak",
    (
        "",
        "Breadboard bravery: GPIO experiments, kiosk boards and reproducible BOM notes.",
    ): (
        "Protoboard ausardia: GPIO saiakerak, kiosko-panelak eta BOM oharrak errepikatzen dira."
    ),
    ("", "Technical blog"): "Blog teknikoa",
    ("", "Back to top"): "Itzuli goialdera",
    ("", "Read article →"): "Irakurri artikulua →",
    ("", "Deploy"): "Hedapena",
    ("", "Shipping Django behind Docker, Gunicorn & nginx"): (
        "Djanga hedapena Docker, Gunicorn eta nginx atzealdean"
    ),
    (
        "",
        "Operational checklist from zero-ish to TLS with backups you can swear by.",
    ): (
        "Egiaztapen zerrenda ia zerotik TLSrekin, sinesten dituzun babeskopiak."
    ),
    ("", "Continue reading →"): "Irakurtzen jarraitu →",
    ("", "Local IA"): "IA lokala",
    (
        "",
        "Responsible local AI workflows you can iterate on nightly",
    ): (
        "Ardurazko IA lokalerako fluxuak — gauero iteratu daitezkeenak"
    ),
    (
        "",
        "Thinking through when modest models outperform giant APIs without leaking payloads.",
    ): (
        "Noiz gainditzen duten modelo xumeek API erraldoiak karga isuri gabe."
    ),
    ("", "Productivity"): "Produktibitatea",
    (
        "",
        "Automating small chores that secretly eat half your roadmap",
    ): (
        "Zure roadmap-aren erdia ezkutuan jaten dituzten lan txikiak automatizatzea"
    ),
    (
        "",
        "Email triage helpers, politely scoped scrapers and sleepy cronfriends that amortize infra.",
    ): (
        "Postaren triaje laguntzaileak, muga orekozko scraperrak eta infra amortizeatzen duten cron "
        "atseginak."
    ),
    ("cta", "Next beat"): "Hurrengo kolpea",
    ("", "Do you have an idea or a process you want to improve?"): (
        "Baduzu hobetu nahi duzun ideia edo prozesuren bat?"
    ),
    (
        "",
        "I can translate it into a web tool, automate the boring limbs or scaffold the whole dependable system.",
    ): (
        "Web tresna bat bihurtu, alderdi aspergarriak automatizatu edo sistema oso "
        "fidagarria muntatu dezaket."
    ),
    ("", "Digital manifesto"): "MANIFESTU DIGITALA",
    (
        "",
        "Values for ethical, sustainable and human technology.",
    ): "Teknologia etiko, jasangarri eta gizatiarrerako balioak.",
    (
        "",
        "A digital community is not only defined by the tools it uses, but by the principles with which it builds, shares and maintains them.",
    ): (
        "Komunitate digital bat ez dute soilik erabiltzen dituen tresnek definitzen, "
        "baizik eta tresna horiek eraikitzeko, partekatzeko eta mantentzeko printzipioek."
    ),
    ("", "Retegi digital values"): "Retegiren balio digitalak",
    ("", "ethics"): "etika",
    ("", "data"): "datuak",
    ("", "human"): "gizakia",
    ("", "open"): "irekia",
    ("", "Ethical artificial intelligence"): "Adimen artifizial etikoa",
    ("", "Digital sovereignty"): "Burujabetza digitala",
    ("", "Privacy by design"): "Pribatutasuna diseinutik",
    ("", "Sustainable technology"): "Teknologia jasangarria",
    ("", "Useful and human software"): "Software erabilgarria eta gizatiarra",
    ("", "Universal accessibility"): "Irisgarritasun unibertsala",
    ("", "Algorithmic transparency"): "Gardentasun algoritmikoa",
    ("", "Meaningful human control"): "Giza kontrol esanguratsua",
    ("", "Open and collaborative culture"): "Kultura irekia eta kolaboratiboa",
    ("", "Responsible security"): "Segurtasun arduratsua",
    ("", "Linguistic and cultural inclusion"): "Hizkuntza eta kultura inklusioa",
    ("", "Independence from digital monopolies"): "Monopolio digitalekiko independentzia",
    ("", "Critical digital literacy"): "Alfabetatze digital kritikoa",
    ("", "Data for the common good"): "Datuak guztion onerako",
    ("", "Technological minimalism"): "Minimalismo teknologikoa",
    ("", "Interoperability"): "Elkarreragingarritasuna",
    ("", "Repairability and maintenance"): "Konpongarritasuna eta mantentzea",
    ("", "Smart decentralization"): "Deszentralizazio adimentsua",
    ("", "Digital wellbeing"): "Ongizate digitala",
    ("", "Technological social responsibility"): "Erantzukizun sozial teknologikoa",
    ("", "Retegi system"): "Retegi sistema",
    ("", "online"): "online",
    ("", "django-admin startproject"): "django-admin startproject",
    ("", "docker compose up -d"): "docker compose up -d",
    ("", "python manage.py deploy"): "python manage.py deploy",
    ("", "API REST online"): "API REST online",
    ("", "RAG assistant ready"): "RAG laguntzailea prest",
    ("", "SSL + Nginx active"): "SSL + Nginx aktibo",
    ("", "AI local"): "IA lokala",
    ("", "Automation"): "Automatizazioa",
    ("", "Django"): "Django",
    ("", "Docker"): "Docker",
    ("", "Nginx"): "Nginx",
    ("", "You:"): "Zu:",
    ("", "Bot:"): "Bot:",
    ("", "Something went wrong."): "Zerbait okerreko gertatu da.",
    ("", "Could not reach the server."): "Ezin izan da zerbitzariarekin konektatu.",
}


def strip_bom(po: polib.POFile) -> None:
    for entry in po:
        entry.msgctxt = (
            entry.msgctxt.replace("\ufeff", "") if entry.msgctxt else entry.msgctxt
        )
        entry.msgstr = (
            entry.msgstr.replace("\ufeff", "") if entry.msgstr else entry.msgstr
        )


def apply_translations(po: polib.POFile, table: dict[tuple[str, str], str]) -> int:
    n = 0
    strip_bom(po)
    for entry in po:
        k = ctxt_key(entry)
        if k in table:
            entry.msgstr = table[k]
            if "fuzzy" in entry.flags:
                entry.flags.remove("fuzzy")
            n += 1
    # Search string (often fuzzy duplicate)
    for entry in po:
        if entry.msgid == "Search" and (entry.msgctxt or "") == "":
            if po.metadata.get("Language", "").startswith("es"):
                entry.msgstr = "Buscar"
            elif po.metadata.get("Language", "").startswith("eu"):
                entry.msgstr = "Bilatu"
            elif po.metadata.get("Language", "").startswith("en"):
                entry.msgstr = "Search"
            if "fuzzy" in entry.flags:
                entry.flags.remove("fuzzy")
    po.metadata.setdefault("MIME-Version", "1.0")
    po.metadata.setdefault("Content-Type", "text/plain; charset=UTF-8")
    return n


def set_language(po: polib.POFile, code: str) -> None:
    po.metadata["Language"] = code


def main() -> int:
    langs = ["es", "eu", "en"]
    tables = {"es": _SPANISH, "eu": _BASELINE}

    if not LOCALE_DIR.is_dir():
        print("locale/ not found", file=sys.stderr)
        return 1

    for code in langs:
        path = LOCALE_DIR / code / "LC_MESSAGES" / "django.po"
        if not path.is_file():
            print(f"Missing {path}", file=sys.stderr)
            continue
        po = polib.pofile(str(path))
        if code == "en":
            set_language(po, "en")
            for entry in po:
                entry.msgstr = entry.msgid
                if "fuzzy" in entry.flags:
                    entry.flags.remove("fuzzy")
            lang_labels = {
                "Euskara": "Basque",
                "Castellano": "Spanish",
                "English": "English",
            }
            for entry in po:
                if (entry.msgctxt or "") != "":
                    continue
                if entry.msgid in lang_labels:
                    entry.msgstr = lang_labels[entry.msgid]
        else:
            set_language(po, code)
            n = apply_translations(po, tables[code])
            print(code, path, "updated entries:", n)

        strip_bom(po)
        po.save(str(path))

    print("done")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
