# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDaesc(RPackage):
    """DAESC is a software for differential allele-specific expression (ASE) analysis 
    using single-cell RNA-seq data of multiple individuals. It can be applied to any 
    comparison represented by a design matrix, including but not limited to: 1) discrete 
    cell types 2) continuous cell states (e.g. pseudotime) 3) case-control disease status 
    4) continuous phenotype of the donors (e.g. BMI, blood pressure). DAESC includes two 
    components: DAESC-BB and DAESC-Mix."""

    homepage = "https://github.com/gqi/DAESC"
    git = "https://github.com/gqi/DAESC.git"

    license("GPL-2")

    version("20240628", commit="af260814982775f8c361e53fb738f637f08857c0")

    depends_on("r@4.0:", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-lme4", type=("build", "run"))
    depends_on("r-aod", type=("build", "run"))
    depends_on("r-statmod", type=("build", "run"))
    depends_on("r-numderiv", type=("build", "run"))
