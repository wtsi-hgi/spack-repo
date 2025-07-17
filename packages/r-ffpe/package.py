# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFfpe(RPackage):
    """Quality assessment and control for FFPE microarray expression data

    Identify low-quality data using metrics developed for expression data derived from Formalin-Fixed, Paraffin-Embedded (FFPE) data.  Also a function for making Concordance at the Top plots (CAT-plots).
    """

    bioc = "ffpe"

    version("1.52.0", commit="d4e86a251c5c2f42e7ab2a234a60dae0a1904b2c")
    version("1.46.0", commit="1c71bd5caa34694db6c01079219c500d071a9cce")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-ttr", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-affy", type=("build", "run"))
    depends_on("r-lumi", type=("build", "run"))
    depends_on("r-methylumi", type=("build", "run"))
    depends_on("r-sfsmisc", type=("build", "run"))
