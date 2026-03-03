# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAgror(RPackage):
	"""Experimental Statistics and Graphics for Agricultural Sciences

	Performs the analysis of completely randomized experimental designs (CRD), randomized blocks (RBD) and Latin square (LSD), experiments in double and triple factorial scheme (in CRD and RBD), experiments in subdivided plot scheme (in CRD and RBD), subdivided and joint analysis of experiments in CRD and RBD, linear regression analysis, test for two samples. The package performs analysis of variance, ANOVA assumptions and multiple comparison test of means or regression, according to Pimentel-Gomes (2009, ISBN: 978-85-7133-055-9), nonparametric test (Conover, 1999, ISBN: 0471160687), test for two samples, joint analysis of experiments according to Ferreira (2018, ISBN: 978-85-7269-566-4) and generalized linear model (glm) for binomial and Poisson family in CRD and RBD (Carvalho, FJ (2019), <doi:10.14393/ufu.te.2019.1244>). It can also be used to obtain descriptive measures and graphics, in addition to correlations and creative graphics used in agricultural sciences (Agronomy, Zootechnics, Food Science and related areas).
	"""
	
	homepage = "https://agronomiar.github.io/AgroR_package/index.html"
	cran = "AgroR" 

	version("1.3.5", md5="0a6a47d93564614d303c6244e39c70fe")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-nortest", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-emmeans", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-multcompview", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-drc", type=("build", "run"))
	depends_on("r-dunn-test", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
