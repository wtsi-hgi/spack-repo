# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySuppa(PythonPackage):
    """A tool to study splicing across multiple conditions at high speed and accuracy."""

    homepage = "https://github.com/comprna/SUPPA"
    pypi = "SUPPA/SUPPA-2.3.tar.gz"

    # Upstream license declared as MIT in setup.py
    license("MIT")

    version("2.2", sha256="7df88a1eeb8f9551b9599678b5958fac72da352b6e17bf1ed084b01c901a076c")
    version("2.2.1", sha256="c09253414d4c3c6e14b65b839030a87f73009b069d7b14b443f79b54e6737dab")
    version("2.2.2", sha256="d5e37df908bf09c28d324e0a8ed70a03604bde5a52966202fdfaab825b3ad243")
    version("2.3", sha256="c7246b0913f627067b714a38f4ec6ea7607404c7baf992c6b9e932c1c91ef738")

    # Build system
    depends_on("py-setuptools", type="build")
    depends_on("python@3.5:", type=("build", "run"))

    # Runtime dependencies from upstream setup.py install_requires
    depends_on("py-scipy@0.15.1:", type=("build", "run"))
    depends_on("py-numpy@1.11.0:", type=("build", "run"))
    depends_on("py-pandas@0.18.0:", type=("build", "run"))
    depends_on("py-statsmodels@0.6.1:", type=("build", "run"))
    depends_on("py-scikit-learn@0.16.1:", type=("build", "run"))

    @run_after("install")
    def install_cli(self):
        # Upstream doesn't install the CLI script or top-level modules.
        # Copy them under libexec and provide a wrapper in bin.
        src = self.stage.source_path
        libexec_dir = join_path(self.prefix.libexec, "suppa")
        mkdirp(libexec_dir)

        # Copy CLI script and its module dependencies
        for fname in (
            "suppa.py",
            "eventGenerator.py",
            "eventClusterer.py",
            "fileMerger.py",
            "psiPerGene.py",
            "psiCalculator.py",
            "significanceCalculator.py",
        ):
            install(join_path(src, fname), libexec_dir)

        # Copy the package directory used by the modules
        install_tree(join_path(src, "lib"), join_path(libexec_dir, "lib"))

        # Write a thin wrapper to invoke the CLI with an augmented PYTHONPATH
        mkdirp(self.prefix.bin)
        wrapper = join_path(self.prefix.bin, "suppa")
        with open(wrapper, "w") as f:
            f.write("#!/bin/bash\n")
            f.write("export PYTHONPATH=\"{0}:$PYTHONPATH\"\n".format(libexec_dir))
            f.write("exec python \"{0}\" \"$@\"\n".format(join_path(libexec_dir, "suppa.py")))
        chmod = which("chmod")
        chmod("+x", wrapper)

    @run_after("install")
    def install_test(self):
        # Basic CLI test: show help
        with working_dir("spack-test", create=True):
            suppa = Executable(join_path(self.prefix.bin, "suppa"))
            suppa("--help")
