# Stratum - Build de 3D Slicer en Windows 11

Instrucciones para compilar 3D Slicer desde código fuente dentro del proyecto `C:\stratum`.

## Estructura esperada

```text
C:\stratum
├─ source
│  ├─ CMakeLists.txt
│  └─ .git
├─ apps
│  └─ SR
├─ workspace
│  └─ build_scripts
├─ extensions
└─ knowledge
```

Uso de carpetas:

```text
C:\stratum\source                 Código fuente de Slicer
C:\stratum\apps\SR                Carpeta de build Release / SuperBuild
C:\stratum\apps\SR\Slicer-build   Carpeta final donde queda Slicer.exe
C:\stratum\workspace\build_scripts Scripts .bat de build
C:\stratum\extensions             Futuras extensiones o módulos
```

---

## 1. Herramientas necesarias

Antes de compilar, el PC debe tener instalado:

```text
Visual Studio 2022 Community
Workload: Desarrollo de escritorio con C++
MSVC v143 x64/x86
Windows 10 SDK o Windows 11 SDK
Git for Windows
Qt 5.15.2 msvc2019_64
Qt WebEngine
CMake
```

En este proyecto se usa el CMake incluido con Visual Studio:

```text
C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\CommonExtensions\Microsoft\CMake\CMake\bin\cmake.exe
```

No se usa `C:\Program Files\CMake\bin\cmake.exe` si esa instalación está rota o pesa 0 bytes.

---

## 2. Abrir la consola correcta

Abrir desde el menú de inicio:

```text
x64 Native Tools Command Prompt for VS 2022
```

No usar PowerShell para lanzar el build principal.

---

## 3. Comprobaciones previas

Desde `x64 Native Tools Command Prompt for VS 2022`:

```bat
where cl
cl

where git
git --version

dir "C:\Program Files\Git\usr\bin\patch.exe"

"C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\CommonExtensions\Microsoft\CMake\CMake\bin\cmake.exe" --version

"C:\Qt\5.15.2\msvc2019_64\bin\qmake.exe" -v

dir C:\Qt\5.15.2\msvc2019_64\lib\cmake\Qt5\Qt5Config.cmake
dir C:\Qt\5.15.2\msvc2019_64\lib\cmake\Qt5WebEngine\Qt5WebEngineConfig.cmake

dir C:\stratum\source\CMakeLists.txt
dir C:\stratum\source\.git
```

Si `CMakeLists.txt` no está en `C:\stratum\source`, comprobar si está en:

```bat
dir C:\stratum\source\Slicer\CMakeLists.txt
```

En ese caso, editar `CommonVars_Stratum_ASCII.bat` y cambiar:

```bat
set "SLICER_SOURCE_DIR=%STRATUM_DIR%\source"
```

por:

```bat
set "SLICER_SOURCE_DIR=%STRATUM_DIR%\source\Slicer"
```

---

## 4. Scripts de build

Los scripts deben estar en:

```text
C:\stratum\workspace\build_scripts
```

Archivos usados:

```text
CommonVars_Stratum_ASCII.bat
Stratum_Release_Build_ASCII.bat
Start_Stratum_Slicer_Release_ASCII.bat
```

`CommonVars_Stratum_ASCII.bat` contiene las rutas del proyecto:

```bat
set "STRATUM_DIR=C:\stratum"
set "SLICER_SOURCE_DIR=%STRATUM_DIR%\source"
set "SLICER_SUPERBUILD_BIN_DIR_REL_X64=%STRATUM_DIR%\apps\SR"
set "SLICER_BIN_DIR_REL_X64=%SLICER_SUPERBUILD_BIN_DIR_REL_X64%\Slicer-build"

set "QT5_DIR_X64=C:/Qt/5.15.2/msvc2019_64/lib/cmake/Qt5"
set "QT5_BIN_DIR=C:\Qt\5.15.2\msvc2019_64\bin"

set "CMAKE_EXE=C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\CommonExtensions\Microsoft\CMake\CMake\bin\cmake.exe"

set "CMAKE_GENERATOR_X64=Visual Studio 17 2022"
set "CMAKE_PLATFORM_X64=x64"

set "GIT_CMD_DIR=C:\Program Files\Git\cmd"
set "GIT_USR_BIN_DIR=C:\Program Files\Git\usr\bin"

set "PATH=%GIT_CMD_DIR%;%GIT_USR_BIN_DIR%;%QT5_BIN_DIR%;%PATH%"
```

---

## 5. Primer build limpio

Desde `x64 Native Tools Command Prompt for VS 2022`:

```bat
cd /d C:\stratum\workspace\build_scripts
Stratum_Release_Build_ASCII.bat clean
```

Esto hace:

```text
1. Carga las variables del proyecto.
2. Comprueba cl.exe, git.exe, patch.exe, CMake y Qt.
3. Borra C:\stratum\apps\SR si existe.
4. Configura CMake.
5. Compila Slicer en Release.
6. Comprueba que se han generado Slicer.exe y SlicerApp-real.exe.
```

La parte de configuración debería acabar con:

```text
Configuring done
Generating done
Build files have been written to: C:/slicerSTRT/apps/SR
```

Después empezará el build real con MSBuild:

```text
Build Release step
MSBuild version ...
```

---

## 6. Build incremental

Para continuar un build interrumpido o recompilar después de cambios pequeños en C++:

```bat
cd /d C:\stratum\workspace\build_scripts
Stratum_Release_Build_ASCII.bat
```

No usar `clean` salvo que quieras borrar todo el build y empezar desde cero.

---

## 7. Comprobar resultado final

Cuando termine el build:

```bat
dir C:\stratum\apps\SR\Slicer-build\Slicer.exe
dir C:\stratum\apps\SR\Slicer-build\bin\Release\SlicerApp-real.exe
```

Deben existir los dos.

Para ejecutar Slicer:

```bat
C:\stratum\apps\SR\Slicer-build\Slicer.exe
```

O usando el script:

```bat
cd /d C:\stratum\workspace\build_scripts
Start_Stratum_Slicer_Release_ASCII.bat
```

---


---

## 8. Cuándo recompilar

| Cambio | Qué hacer |
|---|---|
| Solo usar Slicer | No recompilar |
| Cambiar `.py` de un módulo | Reload en Slicer |
| Cambiar `.ui` de un módulo Python | Reload o reiniciar Slicer |
| Cambiar C++ | Build incremental |
| Cambiar `CMakeLists.txt` | Ejecutar script de build sin `clean` |
| Añadir librería C++ | Ejecutar script de build sin `clean`; si falla, usar `clean` |
| Build corrupto o errores raros | `Stratum_Release_Build_ASCII.bat clean` |

---

## 9. Desarrollo de módulos Python

Si se crea un módulo Python dentro de:

```text
C:\stratum\extensions
```

normalmente no hace falta recompilar Slicer.

Después de modificar un `.py`:

```python
slicer.util.reloadScriptedModule("NombreDelModulo")
```

O usar el botón:

```text
Reload
Reload and Test
```

desde el módulo dentro de Slicer.

Si se modifica un `.ui` y el reload no refresca bien la interfaz, cerrar y abrir Slicer.


## Local Slicer build tree

`C:\stratum\apps\SR` contains the local Slicer SuperBuild/build tree.

This folder is generated by the Slicer build process and contains Visual Studio projects, external dependencies, compiled libraries, temporary build folders, downloaded archives, install folders, and the final Slicer build output.

Important paths:

* Slicer build tree: `C:\stratum\apps\SR`
* Slicer executable: `C:\stratum\apps\SR\Slicer-build\Slicer.exe`
* Upstream Slicer source: `C:\stratum\source`
* STRATUM extension code: `C:\stratum\extensions\slicerSTRT`

Do not commit `apps/SR` to Git. It is a local generated build tree.

For normal scripted module development, edit the extension code under `extensions/slicerSTRT` and reload the module from Slicer Developer Mode. Do not edit files directly inside `apps/SR` unless you are debugging the Slicer build itself.

---

## 10. Sobre CopyDLLs.bat

`CopyDLLs.bat` sirve para copiar DLLs, por ejemplo `vtk*.dll`, desde carpetas internas del build hacia la carpeta donde la aplicación puede encontrarlas.

No ejecutarlo por defecto.

Solo usar algo así si al abrir Slicer aparece un error de DLL faltante:

```text
The code execution cannot proceed because X.dll was not found
```

Para este proyecto, primero probar siempre:

```bat
C:\stratum\apps\SR\Slicer-build\Slicer.exe
```

Si abre correctamente, no hace falta copiar DLLs manualmente.
