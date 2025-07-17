# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHybridmtest(RPackage):
    """Hybrid Multiple Testing

    Performs hybrid multiple testing that incorporates method selection and assumption evaluations into the analysis using empirical Bayes probability (EBP) estimates obtained by Grenander density estimation. For instance, for 3-group comparison analysis, Hybrid Multiple testing considers EBPs as weighted EBPs between F-test and H-test with EBPs from Shapiro Wilk test of normality as weigth. Instead of just using EBPs from F-test only or using H-test only, this methodology combines both types of EBPs through EBPs from Shapiro Wilk test of normality. This methodology uses then the law of total EBPs.
    """

    bioc = "HybridMTest"

    version("1.52.0", commit="94c1c77f2f603749bf87e78d28cb3249d31dbe5d")
    version("1.46.0", commit="2bc99d8b5703e37d83b79bbce443ad3d847f62af")

    depends_on("r@2.9:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-fdrtool", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-survival", type=("build", "run"))
