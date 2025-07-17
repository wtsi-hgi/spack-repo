# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGwastools(RPackage):
    """Tools for Genome Wide Association Studies

    Classes for storing very large GWAS data sets and annotation, and functions for GWAS data cleaning and analysis.
    """

    homepage = "https://github.com/smgogarten/GWASTools"
    bioc = "GWASTools"

    version("1.54.0", commit="9cd2d2d89ad9f4f03cb948a7734696bf5a2d9bb3")
    version("1.48.0", commit="1eb1398d6183146549c28732ea28ce54beec0bc8")

    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-gdsfmt", type=("build", "run"))
    depends_on("r-dbi", type=("build", "run"))
    depends_on("r-rsqlite", type=("build", "run"))
    depends_on("r-gwasexacthw", type=("build", "run"))
    depends_on("r-dnacopy", type=("build", "run"))
    depends_on("r-survival", type=("build", "run"))
    depends_on("r-sandwich", type=("build", "run"))
    depends_on("r-lmtest", type=("build", "run"))
    depends_on("r-logistf", type=("build", "run"))
    depends_on("r-quantsmooth", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
