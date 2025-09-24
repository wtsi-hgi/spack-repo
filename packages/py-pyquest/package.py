# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPyquest(PythonPackage):
    """A Python interface for QuEST."""

    homepage = "https://github.com/cancerit/pyQUEST"

    # Upstream publishes only wheels on PyPI; use GitHub source tarballs
    version(
        "1.1.0",
        sha256="9f6431aff3cb3af09b732abe043a26a7301e14eb1a6c8dd140322a89129264ad",
        url="https://github.com/cancerit/pyQUEST/archive/refs/tags/1.1.0.tar.gz",
    )
    version(
        "1.0.0",
        sha256="08402126eb36b66c0c17683ac9a2e5d31152c70ce2d12139276ada8cce41c01c",
        url="https://github.com/cancerit/pyQUEST/archive/refs/tags/1.0.0.tar.gz",
    )

    license("GPL-3.0-or-later")

    depends_on("py-setuptools", type="build")
    depends_on("python@3.11:", type=("build", "run"))

    # Runtime dependencies from pyproject.toml
    depends_on("py-click", type=("build", "run"))
    depends_on("py-click-option-group", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pysam", type=("build", "run"))
    depends_on("py-python-magic", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            # Provide a basic CLI smoke test
            pyquest = Executable(join_path(self.prefix.bin, "pyquest"))
            pyquest("--help")
