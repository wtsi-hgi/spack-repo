# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RStatgengwas(RPackage):
    """Fast single trait Genome Wide Association Studies (GWAS) following the method described in Kang et al. (2010)."""

    homepage = "https://biometris.github.io/statgenGWAS/index.html"
    cran = "statgenGWAS"

    version("1.0.9", sha256="3b6f9ccad0d19ca46955722c226683f1ca18b9ddefabb04831b4f23dd0fa5247")
    version("1.0.8", sha256="18094ef8fe21fc3b7cd8d1bce45a294d434faa31761500c7b3f13e166c9d5b58")
    version("1.0.7", sha256="2d46894e9be6acbe411d6200a71f1b6644cb21b6e67af563fbdef6eaef06e4f8")
    version("1.0.6", sha256="2ba06064aa3b63335c7c514d108a4e4f6e978d3ba05648ba90b3f6970e59f7ec")
    version("1.0.5", sha256="96abbfb3c5bb0dc1f80f7831a5ea76c921160657e8eb7dc8a2ba51d22c615db9")
    version("1.0.4", sha256="e3e27a066de616aba9ae90c4a8682ce55bd7676dcb1e43f66cda3f784d95bd42")
    version("1.0.3", sha256="2df589a3c70b57a06ff827af79893b67a33fac718fa7d2d92aad84a8b320a7c7")
    version("1.0.2", sha256="6c87e6e497fc2a12c0131fc21f6ff3b8e39f0d86686957d6c95d5f028c714312")
    version("1.0.1", sha256="f9e62f6973bd81508c9c1a4f641f3d83cda9ff82b721f4c1f9f02c2511ced30f")

    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-ggplot2@3.0.0:", type=("build", "run"))
    depends_on("r-sommer@3.7.3:", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-rcpparmadillo", type=("build", "run"))
