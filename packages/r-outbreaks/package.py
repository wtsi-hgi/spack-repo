# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class ROutbreaks(RPackage):
    """Empirical or simulated disease outbreak data, provided either as RData or as text files."""

    homepage = "https://github.com/reconhub/outbreaks"
    cran = "outbreaks"

    version("1.9.0", sha256="3b840bc298581dab80f0b6a1109d2c5477413f6009e74524ba39b4cd7e26d974")
    version("1.5.0", sha256="0db8d495c082912ef66e62d9c88ae70c8add724c239626179bce16032d4d6600")
    version("1.3.0", sha256="01bdcdac7905547bdd3f9dab376286e55d73650c1fed28efa488b7cd4d4f0fcc")
    version("1.2.0", sha256="2d7cb2d72a6cf7d8dbe6a62859d96e6004f20c97be1faf46c2bb304a5967deea")
    version("1.1.0", sha256="5018d0a0811bf58c95a7e01aa05531e6fe3779bef25bbcdc2f0eb664554287e6")
    version("1.0.0", sha256="8fcd30ad7e01f61ecad189cfd0dd6f7f2e76b7ab357460d6e8ffbea98e845918")

    depends_on("r-testthat", type=("build", "run"))
    depends_on("r-covr", type=("build", "run"))
    depends_on("r-ape", type=("build", "run"))
