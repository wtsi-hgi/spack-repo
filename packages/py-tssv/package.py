# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyTssv(PythonPackage):
    """Targeted characterisation of short structural variation."""

    homepage = "https://pypi.org/project/tssv/"
    pypi = "tssv/tssv-1.1.2.tar.gz"

    version("1.1.0", sha256="833b2a559f9e3a1ddf36f5202138da65b5f930a4cbe4f142590e590a5c96739a")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

