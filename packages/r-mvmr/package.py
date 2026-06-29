# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvmr(RPackage):
    """Perform multivariable Mendelian randomization analyses in R."""

    homepage = "https://github.com/WSpiller/MVMR"
    url = "https://github.com/WSpiller/MVMR/archive/refs/tags/v0.4.6.tar.gz"

    license("GPL-3.0-or-later")

    version("0.4.6", sha256="f5a54e7f45d819081a21bc448277664f447f6e2fe94820a6fe6dfcca1856d30e")
    version("0.4.5", sha256="2e68ff6b0b6a7c6439d36b6dd0b9c86ca2536ef34ae329e1f85596636547d842")
    version("0.4.4", sha256="4c40b5ef5d410b77d7093aeb71fda5745554db617dd48bfd544fa470698bc7e8")
    version("0.4.3", sha256="7bd5e24fd1443da79417992443b230c71ee4daefe9853fa81b6cbff1e09cf26b")
    version("0.4.2", sha256="b15c327fe1e91a0cdd309abfa4c2b5f9f58a164cc52139899039e598989dc6d6")
    version("0.4.1", sha256="0faf7cb412a6a6907be7dbd1a0e6a989b87a43b31d1412b137854c4e4cf4bb9a")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-boot", type=("build", "run"))
    depends_on("r-parallelly", type=("build", "run"))
