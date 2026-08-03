# Setup de GitHub — Paso a paso

Guía para dejar el repositorio listo para trabajar entre Joseph y Esteban.

---

## 1. Crear el repositorio en GitHub

**Uno solo de los dos** hace esto (recomiendo Joseph, como owner):

1. Entra a https://github.com/new
2. Configura así:

| Campo | Valor |
|---|---|
| Repository name | `solarquote` |
| Description | `Sistema web de cotización de estructuras fotovoltaicas — HEXtructure S.A.S.` |
| Visibility | **Private** (cámbialo a público al final si quieren) |
| Add a README file | ❌ **NO marcar** (ya tenemos uno) |
| Add .gitignore | ❌ **NO marcar** (ya tenemos uno) |
| Choose a license | ❌ None |

3. Click en **Create repository**
4. **No cierres la página** — vas a necesitar la URL que aparece

---

## 2. Agregar a Esteban como colaborador

En el repo recién creado:

1. **Settings** → **Collaborators** (menú izquierdo)
2. Click **Add people**
3. Busca el usuario de GitHub de Esteban
4. Rol: **Write**
5. Esteban recibe un email — tiene que aceptar la invitación

---

## 3. Subir el proyecto (solo Joseph, una vez)

Abre una terminal en la carpeta `solarquote`:

```bash
cd "C:\Users\ROG\Desktop\SolarQuote\SolarQuote\solarquote"

# Inicializar git
git init

# Configurar tu identidad (si no lo has hecho antes)
git config user.name "Joseph Flores"
git config user.email "josephaugustoflores@gmail.com"

# Primer commit
git add .
git commit -m "chore: estructura inicial del monorepo"

# Conectar con GitHub
git branch -M main
git remote add origin https://github.com/NotGuatas/solarquote.git
git push -u origin main

# Crear la rama develop
git checkout -b develop
git push -u origin develop
```

> Si te pide usuario y contraseña: GitHub ya no acepta contraseña.
> Necesitas un **Personal Access Token**. Ver sección 6 abajo.

---

## 4. Proteger las ramas `main` y `develop`

Esto evita que alguien suba código roto directo a producción.

En GitHub: **Settings** → **Branches** → **Add branch ruleset**

### Regla para `main`

| Opción | Valor |
|---|---|
| Ruleset Name | `proteger-main` |
| Enforcement status | **Active** |
| Target branches | Add target → `main` |

Marca estas reglas:
- ✅ **Restrict deletions**
- ✅ **Require a pull request before merging**
  - Required approvals: **1**
- ✅ **Block force pushes**

### Regla para `develop`

Igual que arriba, pero:
- Ruleset Name: `proteger-develop`
- Target branches: `develop`
- Required approvals: **1**

> **Nota:** en repos privados con plan gratuito, las branch rules pueden estar limitadas.
> Si no te deja, cambia el repo a **público** o simplemente acuerden por confianza:
> *nadie hace push directo a `main` ni a `develop`.*

---

## 5. Esteban clona el repositorio

Una vez que aceptó la invitación:

```bash
git clone https://github.com/NotGuatas/solarquote.git
cd solarquote

# Configurar identidad
git config user.name "Esteban Narváez"
git config user.email "<su-email>"

# Traer la rama develop
git checkout develop
```

---

## 6. Personal Access Token (si git pide contraseña)

GitHub eliminó el login por contraseña. Necesitas un token:

1. https://github.com/settings/tokens → **Generate new token (classic)**
2. Note: `solarquote-local`
3. Expiration: **90 days** (o `No expiration` si prefieren)
4. Scopes: marca **`repo`** (completo)
5. **Generate token** → cópialo (solo se muestra una vez)
6. Cuando git te pida contraseña, pega el token

**Para no tener que pegarlo cada vez:**

```bash
git config --global credential.helper manager
```

---

## 7. Verificar que todo quedó bien

```bash
# Ver ramas remotas
git branch -r
# Debe mostrar: origin/main y origin/develop

# Ver el remote
git remote -v
# Debe mostrar la URL de GitHub

# Ver estado
git status
# Debe decir "nothing to commit, working tree clean"
```

---

## Checklist de este paso

- [ ] Repo `solarquote` creado en GitHub
- [ ] Esteban agregado como colaborador (rol Write)
- [ ] Esteban aceptó la invitación
- [ ] Código subido a `main`
- [ ] Rama `develop` creada y subida
- [ ] Ramas `main` y `develop` protegidas
- [ ] Esteban clonó el repo y está en `develop`
- [ ] Los dos pueden hacer `git pull` sin errores

---

## Regla de oro del equipo

> **Nunca trabajen directo en `main` ni en `develop`.**
> Siempre: rama nueva → commit → push → Pull Request → review del otro → merge.
