# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNumpySugar(PythonPackage):
    """Missing NumPy functionalities."""

    homepage = "https://github.com/limix/numpy-sugar"
    pypi = "numpy_sugar/numpy_sugar-1.5.4.tar.gz"

    version("1.5.4", sha256="0d2a8d1d8c21f33d40c6a4fed1d11157e970f2d49581812c9613e52c1c7989ac")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-numpy@1.18.5:", type=("build", "run"))
    depends_on("py-scipy@1.4.1:", type=("build", "run"))
    depends_on("py-pytest@6.1.2:", type=("build", "run"))
    depends_on("py-pytest@6.1.2:", type=("build", "run"))
    depends_on("py-black@22.12.0:", type=("build", "run"))
    depends_on("py-isort@5.11.4:", type=("build", "run"))
    depends_on("py-pyright@1.1.288:", type=("build", "run"))
    depends_on("py-poetry", type=("build", "run"))
