# SolarQuote

Sistema web para la gestión y cotización de estructuras fotovoltaicas de **HEXtructure S.A.S.**

Proyecto Capstone — Universidad de Las Américas, Ingeniería de Software
Autores: Joseph Flores · Esteban Narváez

---

## Arquitectura

Arquitectura desacoplada de 5 contenedores:

| Contenedor | Tecnología | Despliegue | Carpeta |
|---|---|---|---|
| Frontend | React + Vite | Vercel | `frontend/` |
| Backend principal | FastAPI | Railway | `backend/` |
| Microservicio IA | FastAPI + Claude API | Railway | `ia-service/` |
| Módulo cálculo/cotización | FastAPI | Railway | `calc-service/` |
| Base de datos | PostgreSQL | Neon | — |

---

## Reparto de módulos

> Cada uno es dueño de su **vertical completa**: frontend + endpoints + lógica de su módulo.

### Trabajo compartido (los dos, primero)
Antes de repartirnos: modelos de base de datos, autenticación JWT, configuración de CI/CD y estructura base de cada servicio.

### Joseph Flores
| Módulo | RFs | Descripción |
|---|---|---|
| **1 — Layout** | RF-01, RF-02, RF-03 | Terreno y caminos, panel e inversor, generación de layout solar |
| **2 — Boceto** | RF-04, RF-05 | Carga y procesamiento de boceto (IA), confirmación y edición |

### Esteban Narváez
| Módulo | RFs | Descripción |
|---|---|---|
| **3 — Cotización** | RF-06, RF-07 | Cálculo de materiales f(L,A,B), generación de proforma Word/Excel |
| **4 — Administración** | RF-08 a RF-13 | Inversores, precios, historial, seguridad, clientes, tablero |
| **5 — Validación** | RF-14, RF-15, RF-16 | Despacho + conteo de varillas (IA), recepción en terreno, seguimiento |

---

## Estrategia de ramas

```
main          ← producción (protegida, solo merge por PR)
 └── develop  ← integración (protegida, solo merge por PR)
      ├── feat/layout-rf01-terreno
      ├── feat/boceto-rf04-carga
      ├── feat/cotizacion-rf06-calculo
      └── fix/nombre-del-bug
```

### Convención de nombres de rama

```
feat/<modulo>-<rf>-<descripcion-corta>
fix/<descripcion-corta>
docs/<descripcion-corta>
refactor/<descripcion-corta>
```

Ejemplos:
- `feat/layout-rf03-generacion-solar`
- `feat/admin-rf09-gestion-precios`
- `fix/cors-railway-vercel`

### Convención de commits

```
<tipo>(<alcance>): <descripción en imperativo>
```

Tipos: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`

Ejemplos:
```
feat(layout): agregar cálculo de área útil descontando caminos
fix(auth): corregir expiración de token JWT
docs(readme): actualizar reparto de módulos
```

### Flujo de trabajo diario

```bash
# 1. Actualizar develop
git checkout develop
git pull origin develop

# 2. Crear tu rama de feature
git checkout -b feat/layout-rf01-terreno

# 3. Trabajar y commitear
git add .
git commit -m "feat(layout): agregar formulario de terreno"

# 4. Subir y abrir PR hacia develop
git push -u origin feat/layout-rf01-terreno
# → Abrir Pull Request en GitHub, pedir review al otro
```

**Regla:** nadie mergea su propio PR sin que el otro lo revise.

---

## Sprints

Sprints de **2 semanas**. Al cierre de cada sprint: merge de `develop` → `main` y deploy.

| Sprint | Épica | Responsable |
|---|---|---|
| S1 | Setup, arquitectura, modelos de datos, auth | Ambos |
| S2–S3 | Módulo Layout | Joseph |
| S4–S5 | Módulo Boceto | Joseph |
| S6–S7 | Módulo Cotización | Esteban |
| S8–S11 | Módulo Administración | Esteban |
| S12–S14 | Módulo Validación | Esteban |
| S15–S16 | Integración y pruebas E2E | Ambos |
| S17–S18 | Estabilización | Ambos |
| S19–S22 | Despliegue pre-producción | Ambos |

---

## Setup local

> Instrucciones detalladas en [`docs/SETUP.md`](docs/SETUP.md)

```bash
git clone https://github.com/NotGuatas/solarquote.git
cd solarquote
```

---

## Estructura del proyecto

```
solarquote/
├── .github/workflows/     # CI/CD (GitHub Actions)
├── frontend/              # React + Vite → Vercel
│   ├── src/
│   │   ├── components/    # Componentes reutilizables
│   │   ├── pages/         # Vistas por módulo
│   │   ├── services/      # Llamadas a API
│   │   ├── hooks/         # Custom hooks
│   │   └── utils/
│   └── public/
├── backend/               # FastAPI principal → Railway
│   └── app/
│       ├── models/        # SQLAlchemy (tablas)
│       ├── schemas/       # Pydantic (validación)
│       ├── routers/       # Endpoints por módulo
│       ├── services/      # Lógica de negocio
│       └── core/          # Config, seguridad, DB
├── ia-service/            # FastAPI IA → Railway
├── calc-service/          # FastAPI cálculo → Railway
└── docs/                  # Documentación técnica
```
