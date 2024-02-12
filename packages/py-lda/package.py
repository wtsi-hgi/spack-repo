# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLda(PythonPackage):
    """lda implements latent Dirichlet allocation (LDA) using collapsed Gibbs sampling."""

    homepage = "https://github.com/lda-project/lda/"
    pypi = "lda/lda-3.0.0.tar.gz"

    version("3.0.0", sha256="c9acbc1c55d2928f7e3e2336352b3382d78e43dbb0d12bf9ed97f87bce6d6708")

    depends_on("py-poetry-core", type="build")
    depends_on("meson", type="build")
    depends_on("py-cython", type="build")

    depends_on("py-numpy@1.13.0:2.0", type=("build", "run"))
