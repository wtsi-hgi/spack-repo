from spack.package import *


class PySubprocess32(Package):
    """Compatibility package for subprocess32.

    On Python 3, subprocess32 is unnecessary. This recipe installs a small
    shim module named ``subprocess32`` that re-exports the standard library
    ``subprocess`` module, avoiding strict Python 2 constraints that cause
    concretization conflicts in unified environments.

    On Python 2 (if ever used), the same shim still provides a usable import,
    though without backported enhancements.
    """

    homepage = "https://pypi.org/project/subprocess32/"

    # Minimal placeholder version to satisfy concretization
    version("0.0")

    # This package installs a shim only; there is no upstream source to fetch.
    has_code = False

    # Keep the interface consistent with other Python packages
    depends_on("python", type=("build", "run"))

    def install(self, spec, prefix):
        # Construct site-packages path matching the selected Python
        py_ver = str(spec["python"].version.up_to(2))
        site_packages = join_path(prefix, "lib", f"python{py_ver}", "site-packages")
        mkdirp(site_packages)

        # Provide a minimal shim so `import subprocess32` works under Python 3
        shim = join_path(site_packages, "subprocess32.py")
        with open(shim, "w") as f:
            f.write(
                "# Auto-generated shim installed by Spack\n"
                "# Maps subprocess32 -> subprocess for compatibility on Python 3+\n"
                "from subprocess import *\n"
            )

    # Minimal package; no additional install-time tests required
