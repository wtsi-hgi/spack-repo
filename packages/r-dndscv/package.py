# Copyright 2013-2025 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDndscv(RPackage):
    """Poisson-based dN/dS models to quantify natural selection in somatic
    evolution. Provides functions for studying selection on coding sequences
    using a Poisson implementation of dN/dS, including context-dependent
    mutation effects and selection on nonsense and splice site mutations."""

    homepage = "https://github.com/im3sanger/dndscv"
    git = "https://github.com/im3sanger/dndscv.git"

    license("GPL-3.0-or-later")

    # Latest commit-based version (use commit date as version per guidelines)
    version("20250515", commit="69007c2bbd2d6dae003a30dcfe5dda3df722b2f8")

    # Base R requirement (DESCRIPTION does not specify an R version)
    depends_on("r", type=("build", "run"))

    # Required imports from DESCRIPTION
    with default_args(type=("build", "run")):
        depends_on("r-seqinr")
        depends_on("r-mass")
        depends_on("r-genomicranges")
        depends_on("r-biostrings")
        depends_on("r-iranges")
        depends_on("r-rsamtools")
        depends_on("r-poilog")
        depends_on("r-plyr")

    # Optional suggests as variants (disabled by default)
    variant("knitr", default=False, description="Enable vignette building with knitr")
    variant("rmarkdown", default=False, description="Enable vignette building with rmarkdown")

    depends_on("r-knitr", when="+knitr", type=("build", "run"))
    depends_on("r-rmarkdown", when="+rmarkdown", type=("build", "run"))

