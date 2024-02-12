# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPybigtools(PythonPackage):
    """Bigtools is a library and associated tools for reading and writing bigwig and bigbed files."""

    homepage = "https://github.com/jackh726/bigtools"
    pypi = "pybigtools/pybigtools-0.1.0.tar.gz"

    version("0.1.0", sha256="ec78aacccf2555f6b41fda78e078738f516441be4f4ab162f110520cf30e6255")

    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-maturin@1.0:2.0", type=("build"))

    def patch(self):
        which("touch")("pybigtools/__init__.py")
