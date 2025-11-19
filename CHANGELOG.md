# CHANGELOG:

## [1.0.2] - 18-11-2025
### Fixed
- Accidentally pushed the wrong build onto pypi. This one has the test suite removed as described for v1.0.1. Also removed utils.py, a legacy file that served no purpose.

## [1.0.1] - 18-11-2025
### Fixed
- Tests included in the package would not work, missing ground truths. Incorporating test suite into package would have required major overhaul of files and project structure. Removed test suite from package because it's not that important. Tests are still available on the official git repo.
