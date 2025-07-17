# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDmrscan(RPackage):
    """Detection of Differentially Methylated Regions

    This package detects significant differentially methylated regions (for both qualitative and quantitative traits), using a scan statistic with underlying Poisson heuristics. The scan statistic will depend on a sequence of window sizes (# of CpGs within each window) and on a threshold for each window size. This threshold can be calculated by three different means: i) analytically using Siegmund et.al (2012) solution (preferred), ii) an important sampling as suggested by Zhang (2008), and a iii) full MCMC modeling of the data, choosing between a number of different options for modeling the dependency between each CpG.
    """

    homepage = "https://github.com/christpa/DMRScan"
    bioc = "DMRScan"

    version("1.30.0", commit="b3a7b1490d8c3335d8988a6e0dbe0fa1e1102a68")
    version("1.24.0", commit="fded05824b2276a3f73c9d49ad27426c4fc77abb")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-rcpproll", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-mvtnorm", type=("build", "run"))
