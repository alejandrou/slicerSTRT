# SLIAFlow Slicer Build On Windows

This document describes the local Windows 11 build setup for the SLIAFlow-related Slicer prototype.

Machine-specific Slicer paths used by repository tooling belong in `config/local.json`. Use `config/local.example.json` as the portable template.

Exact Qt and CMake paths belong in local build scripts or local environment variables, not in `config/local.json`.

## Prerequisites

- Windows 11.
- Visual Studio 2022 with the Desktop development with C++ workload.
- MSVC v143 x64/x86 tools.
- Windows 10 SDK or Windows 11 SDK.
- Git for Windows, including `patch.exe`.
- Qt 5.15.2 for MSVC 2019 64-bit, including Qt WebEngine.
- CMake. The Visual Studio bundled CMake is acceptable when the standalone CMake installation is unavailable or broken.

## Local Configuration

Copy `config/local.example.json` to `config/local.json` and set the local paths for:

- `slicerSourceDirectory`: local Slicer source tree.
- `slicerBuildDirectory`: local Slicer SuperBuild/build tree.
- `slicerExecutable`: built Slicer executable.
- `slicerSkillDirectory`: installed Slicer skill, when used outside repository docs.

`config/local.json` is private local configuration and must remain ignored by Git.

## Expected Repository Areas

- `source/`: local Slicer source reference.
- `apps/`: local application and build outputs.
- `apps/SR/`: conventional local Slicer SuperBuild/build tree for this workspace.
- `apps/SR/Slicer-build/`: conventional final Slicer build output.
- `workspace/build_scripts/`: optional local build helper scripts.
- `extensions/`: SLIAFlow-specific Slicer extension code.

The `apps/` build tree is generated output. Do not commit it.
The `workspace/` tree is ignored local material. Scripts under `workspace/build_scripts/` may contain machine-specific paths, are not guaranteed to exist in every clone, and local paths must not be committed.

## Configure The Build

Use the x64 Native Tools Command Prompt for VS 2022 for the main build.

Choose machine-specific values for the source, build, and Qt directories. The following examples use temporary command-prompt variables and do not modify repository configuration:

```bat
set "SLICER_SOURCE_DIR=<repository>\source"
set "SLICER_BUILD_DIR=<repository>\apps\SR"
set "QT_ROOT=<Qt 5.15.2 msvc2019_64 directory>"
set "QT5_DIR=%QT_ROOT%\lib\cmake\Qt5"
```

If the checkout is under `source\Slicer`, set `SLICER_SOURCE_DIR` to that directory instead.

Before configuring, verify the compiler, Git tools, CMake, source layout, and Qt installation:

```bat
where cl
where git
where patch
cmake --version
git -C "%SLICER_SOURCE_DIR%" rev-parse --is-inside-work-tree
dir "%SLICER_SOURCE_DIR%\CMakeLists.txt"
dir "%QT_ROOT%\bin\qmake.exe"
"%QT_ROOT%\bin\qmake.exe" -v
dir "%QT5_DIR%\Qt5Config.cmake"
dir "%QT_ROOT%\lib\cmake\Qt5WebEngine\Qt5WebEngineConfig.cmake"
```

Every command must succeed before configuring. Store permanent Qt and CMake paths in local build scripts or local environment variables, not in repository-wide instructions or unsupported `config/local.json` fields.

If the Slicer source checkout is nested differently on a local machine, update the local configuration or build script variables rather than changing repository documentation.

## Portable Command-Line Fallback

The ignored helper scripts are convenient but are not required. The following commands implement the same configure and build sequence from an x64 Native Tools Command Prompt for VS 2022.

Configure a new or existing SuperBuild tree:

```bat
cmake -G "Visual Studio 17 2022" -A x64 -DQt5_DIR:PATH="%QT5_DIR%" -S "%SLICER_SOURCE_DIR%" -B "%SLICER_BUILD_DIR%"
if errorlevel 1 exit /b 1
if not exist "%SLICER_BUILD_DIR%\CMakeCache.txt" exit /b 1
```

A successful configure reports `Configuring done` and `Generating done`, identifies `%SLICER_BUILD_DIR%` as the build-file destination, and creates `%SLICER_BUILD_DIR%\CMakeCache.txt`.

Build or continue the Release build incrementally:

```bat
cmake --build "%SLICER_BUILD_DIR%" --config Release
if errorlevel 1 exit /b 1
```

The build should start MSBuild and return exit code `0`. Re-running the same command continues an interrupted build or rebuilds changed targets without deleting completed external projects.

## Local Build Helper Scripts

When the optional local scripts exist, run them from the x64 Native Tools Command Prompt for VS 2022.

Clean build:

```bat
cd /d <repository>\workspace\build_scripts
SLIAFlow_Release_Build_ASCII.bat clean
```

Incremental build:

```bat
cd /d <repository>\workspace\build_scripts
SLIAFlow_Release_Build_ASCII.bat
```

Optional launcher:

```bat
cd /d <repository>\workspace\build_scripts
Start_SLIAFlow_Slicer_Release_ASCII.bat
```

After a successful build, verify that these executables exist:

```bat
dir "%SLICER_BUILD_DIR%\Slicer-build\Slicer.exe"
dir "%SLICER_BUILD_DIR%\Slicer-build\bin\Release\SlicerApp-real.exe"
if not exist "%SLICER_BUILD_DIR%\Slicer-build\Slicer.exe" exit /b 1
if not exist "%SLICER_BUILD_DIR%\Slicer-build\bin\Release\SlicerApp-real.exe" exit /b 1
```

## Clean Build

A clean build removes the local build tree and configures Slicer from scratch.

Use a clean build when:

- configuring the project for the first time;
- the build tree is corrupted;
- dependency paths changed;
- an incremental build cannot recover.

The conventional local target is `apps/SR/`, with the final executable under `apps/SR/Slicer-build/`.

For a command-line clean build, remove only the configured generated build tree, then run the portable configure and build commands again:

```bat
if exist "%SLICER_BUILD_DIR%" rmdir /s /q "%SLICER_BUILD_DIR%"
cmake -G "Visual Studio 17 2022" -A x64 -DQt5_DIR:PATH="%QT5_DIR%" -S "%SLICER_SOURCE_DIR%" -B "%SLICER_BUILD_DIR%"
if errorlevel 1 exit /b 1
cmake --build "%SLICER_BUILD_DIR%" --config Release
if errorlevel 1 exit /b 1
```

Before running `rmdir`, confirm that `SLICER_BUILD_DIR` resolves to the intended generated Slicer build tree. Never point it at the repository root, source tree, extension source, or a directory containing irreplaceable files.

## Incremental Build

Use an incremental build after small source or CMake changes when the build tree is healthy.

Do not clean by default. A clean rebuild can be expensive because Slicer uses a SuperBuild with external dependencies.

## Executable

The conventional local executable is:

```text
apps/SR/Slicer-build/Slicer.exe
apps/SR/Slicer-build/bin/Release/SlicerApp-real.exe
```

If a local machine uses a different build tree, set `slicerExecutable` in `config/local.json`.

Launch the built wrapper executable directly:

```bat
start "" "%SLICER_BUILD_DIR%\Slicer-build\Slicer.exe"
```

## Reload Versus Rebuild

| Change | Recommended action |
|---|---|
| Use Slicer without code changes | No rebuild |
| Python scripted module `.py` change | Reload or Reload and Test in Slicer |
| Python scripted module `.ui` change | Reload; restart Slicer if the UI does not refresh cleanly |
| C++ change | Incremental build |
| `CMakeLists.txt` change | Reconfigure or run the build script without cleaning first |
| New C++ library or dependency path change | Reconfigure; clean only if incremental recovery fails |
| Corrupted build tree or unresolved generated-state errors | Clean build |

## Scripted Module Development

Normal SLIAFlow extension work should happen under `extensions/`.

For Python scripted modules, a full Slicer rebuild is usually not required. Start Slicer, enable Developer Mode, open the module, then use Reload or Reload and Test.

## Troubleshooting

If Slicer reports a missing DLL, first try launching the built executable from the configured Slicer build output. Only copy DLLs manually when the build output is known to be incomplete and the missing library source is understood.

If CMake cannot find Qt, check the Qt CMake package directory and update local build configuration.

If `cl`, `git`, `patch`, or CMake cannot be found, use the Visual Studio native tools prompt and verify local `PATH` setup.
