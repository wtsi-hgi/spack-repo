# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRipat(RPackage):
    """Retroviral Integration Pattern Analysis Tool (RIPAT)

    RIPAT is developed as an R package for retroviral integration sites annotation and distribution analysis. RIPAT needs local alignment results from BLAST and BLAT. Specific input format is depicted in RIPAT manual. RIPAT provides RV integration pattern analysis result as forms of R objects, excel file with multiple sheets and plots.
    """

    homepage = "https://github.com/bioinfo16/RIPAT/"
    bioc = "RIPAT"

    version("1.12.0", commit="ed95547f6e507d1cf6c7ae139fd65e28590739fa")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-biomart@2.38:", type=("build", "run"))
    depends_on("r-genomicranges@1.34:", type=("build", "run"))
    depends_on("r-ggplot2@3.1:", type=("build", "run"))
    depends_on("r-iranges@2.16:", type=("build", "run"))
    depends_on("r-karyoploter@1.6.3:", type=("build", "run"))
    depends_on("r-openxlsx@4.1.4:", type=("build", "run"))
    depends_on("r-plyr@1.8.4:", type=("build", "run"))
    depends_on("r-regioner@1.12:", type=("build", "run"))
    depends_on("r-rtracklayer@1.42.2:", type=("build", "run"))
    depends_on("r-stringr@1.3.1:", type=("build", "run"))
