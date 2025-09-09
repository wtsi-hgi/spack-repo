# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyLuca(PythonPackage):
    """Locus-based Universal CRISPR Aligner (LUCA)."""

    homepage = "https://github.com/cancerit/LUCA"

    # Source releases are on GitHub tags
    version(
        "1.0.2",
        sha256="7562eff9e59096f3c48247367bcd882a7936ec7ade51be2b1fd1ef0663247729",
        url="https://github.com/cancerit/LUCA/archive/refs/tags/1.0.2.tar.gz",
    )
    version(
        "1.0.1",
        sha256="6da37383af972f2679d06ea23f45e1bfd99eb9c4318ef3eb4eebebb4430164d9",
        url="https://github.com/cancerit/LUCA/archive/refs/tags/1.0.1.tar.gz",
    )
    version(
        "1.0.0",
        sha256="50ad6a1165d655447767f55b5386c709d70f73309db34b408eeea390f8d5859b",
        url="https://github.com/cancerit/LUCA/archive/refs/tags/1.0.0.tar.gz",
    )

    license("GPL-3.0-only")

    # Build system
    depends_on("py-setuptools", type="build")
    depends_on("python@3.11:", type=("build", "run"))

    # Runtime dependencies from pyproject.toml
    depends_on("py-charset-normalizer@3.3.0:", type=("build", "run"))
    depends_on("py-click@8.1.7:", type=("build", "run"))
    depends_on("py-click-option-group@0.5.4:", type=("build", "run"))
    depends_on("py-numpy@2.0:", type=("build", "run"))
    depends_on("py-pydantic@2.10.1:", type=("build", "run"))
    depends_on("py-pysam@0.22.1:", type=("build", "run"))
    depends_on("py-python-magic@0.4.24:", type=("build", "run"))
    depends_on("py-pyyaml@6.0:", type=("build", "run"))

    # Optional test dependencies
    variant("test", default=False, description="Enable test dependencies")
    depends_on("py-pytest@8.4.1:", type=("build", "run"), when="+test")
    depends_on("py-pytest-cov@6.2.1:", type=("build", "run"), when="+test")
    depends_on("py-pycodestyle@2.14.0:", type=("build", "run"), when="+test")

    @run_after("install")
    def install_test(self):
        # Basic CLI and import tests to verify installation
        with working_dir("spack-test", create=True):
            # CLI should be available
            luca = Executable(join_path(self.prefix.bin, "luca"))
            luca("--help")
            # Module import should succeed
            python = which("python")
            python("-c", "import luca")
