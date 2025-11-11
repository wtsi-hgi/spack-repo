# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os


class PySuppa(Package):
    """A tool to study splicing across multiple conditions at high speed and accuracy."""

    homepage = "https://github.com/comprna/SUPPA"
    pypi = "SUPPA/SUPPA-2.3.tar.gz"

    # Upstream license declared as MIT in setup.py
    license("MIT")

    version("2.4", sha256="d30ab32dfe504085f658c6867c36d8265a497c0febfaabfab278a90091ad1a6d", url="https://github.com/comprna/SUPPA/archive/refs/tags/v2.4.zip")
    version("2.2", sha256="7df88a1eeb8f9551b9599678b5958fac72da352b6e17bf1ed084b01c901a076c")
    version("2.2.1", sha256="c09253414d4c3c6e14b65b839030a87f73009b069d7b14b443f79b54e6737dab")
    version("2.2.2", sha256="d5e37df908bf09c28d324e0a8ed70a03604bde5a52966202fdfaab825b3ad243")
    version("2.3", sha256="c7246b0913f627067b714a38f4ec6ea7607404c7baf992c6b9e932c1c91ef738")

    # Runtime dependencies from upstream setup.py (for older versions)
    # and documentation. v2.4 ships without a setup.py, so we install
    # files manually and require Python + deps at runtime.
    depends_on("python@3.5:", type=("build", "run"))
    depends_on("py-scipy@0.15.1:", type=("build", "run"))
    depends_on("py-numpy@1.11.0:", type=("build", "run"))
    depends_on("py-pandas@0.18.0:", type=("build", "run"))
    depends_on("py-statsmodels@0.6.1:", type=("build", "run"))
    depends_on("py-scikit-learn@0.16.1:", type=("build", "run"))

    def install(self, spec, prefix):
        # Manual install: copy CLI, modules, and helper scripts to libexec
        # and provide a wrapper in bin that sets PYTHONPATH.
        import glob

        src = self.stage.source_path
        libexec_dir = join_path(prefix.libexec, "suppa")
        mkdirp(libexec_dir)

        # Copy core Python/Perl entry scripts present in releases
        for pattern in ("*.py", "*.pl"):
            for path in glob.glob(join_path(src, pattern)):
                install(path, libexec_dir)

        # Copy library and scripts directories when present
        if os.path.isdir(join_path(src, "lib")):
            install_tree(join_path(src, "lib"), join_path(libexec_dir, "lib"))
        if os.path.isdir(join_path(src, "scripts")):
            install_tree(join_path(src, "scripts"), join_path(libexec_dir, "scripts"))

        # Write a thin wrapper to invoke the CLI with an augmented PYTHONPATH
        mkdirp(prefix.bin)
        wrapper = join_path(prefix.bin, "suppa.py")
        py_exe = "python"
        if "python" in spec:
            try:
                py_exe = spec["python"].command.path
            except Exception:
                py_exe = join_path(spec["python"].prefix.bin, "python")
        with open(wrapper, "w") as f:
            f.write("#!/bin/bash\n")
            f.write("export PYTHONPATH=\"{0}:$PYTHONPATH\"\n".format(libexec_dir))
            f.write("exec {0} \"{1}\" \"$@\"\n".format(py_exe, join_path(libexec_dir, "suppa.py")))
        chmod = which("chmod")
        chmod("+x", wrapper)

    @run_after("install")
    def install_test(self):
        # Basic CLI test: show help
        with working_dir("spack-test", create=True):
            suppa = Executable(join_path(self.prefix.bin, "suppa.py"))
            suppa("--help")
