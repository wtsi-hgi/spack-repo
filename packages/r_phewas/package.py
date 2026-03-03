# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RPhewas(RPackage):
    """The PheWAS R package is designed to provide an accessible interface to the phenome wide association study."""

    homepage = "https://github.com/PheWAS/PheWAS/"
    url = "https://github.com/PheWAS/PheWAS/archive/refs/tags/v0.99.6-1.tar.gz"

    version("0.99.6-1", sha256="d462db49cd32dcbacc8e1f0e4611f1e1de21a7e9e227f0d53a63de16272533c7")
    version("0.12.3", sha256="2d8145821fa043785c15313aef0f37b12e8f8e86c11dc70fc4087f0fd8dd5e64")
    version("0.12.2-2", sha256="55fb1dabe0b4f50b4c8347bc0198f9cc915ee6605ee740da22fd93c378ced872")
    version("0.12", sha256="7063af0c3759e37e44f4ee2b92e22e579d9c58e15f0a529de593540489878544")

    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-meta", type=("build", "run"))
    depends_on("r-ggrepel", type=("build", "run"))
    depends_on("r-dt", type=("build", "run"))
    depends_on("r-survival", type=("build", "run"))
    depends_on("r-logistf", type=("build", "run"))
    depends_on("r-lmtest", type=("build", "run"))
