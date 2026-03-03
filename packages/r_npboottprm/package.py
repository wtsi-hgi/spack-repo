# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNpboottprm(RPackage):
	"""Nonparametric Bootstrap Test with Pooled Resampling

	Addressing crucial research questions often necessitates a small
    sample size due to factors such as distinctive target populations, rarity
    of the event under study, time and cost constraints, ethical concerns, or
    group-level unit of analysis. Many readily available analytic methods,
    however, do not accommodate small sample sizes, and the choice of the best
    method can be unclear. The 'npboottprm' package enables the execution of
    nonparametric bootstrap tests with pooled resampling to help fill this gap.
    Grounded in the statistical methods for small sample size studies detailed
    in Dwivedi, Mallawaarachchi, and Alvarado (2017) <doi:10.1002/sim.7263>, the
    package facilitates a range of statistical tests, encompassing independent
    t-tests, paired t-tests, and one-way Analysis of Variance (ANOVA) F-tests.
    The nonparboot() function undertakes essential computations, yielding
    detailed outputs which include test statistics, effect sizes, confidence
    intervals, and bootstrap distributions. Further, 'npboottprm' incorporates
    an interactive 'shiny' web application, nonparboot_app(), offering intuitive,
    user-friendly data exploration.
	"""
	
	homepage = "https://github.com/mightymetrika/npboottprm"
	cran = "npboottprm" 

	version("0.2.1", md5="8e9d9fd32654665fc067eae5aaa57690")
	version("0.2.0", md5="5cc251a2592fdf0f7887bb8a463d78e0")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-fgarch", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lmperm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mkinfer", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-sn", type=("build", "run"))
