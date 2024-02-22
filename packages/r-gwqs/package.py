# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGwqs(RPackage):
	"""Generalized Weighted Quantile Sum Regression

	Fits Weighted Quantile Sum (WQS) regression  (Carrico et al. (2014) <doi:10.1007/s13253-014-0180-3>), a random subset implementation of WQS (Curtin et al. (2019) <doi:10.1080/03610918.2019.1577971>), a repeated holdout validation WQS (Tanner et al. (2019) <doi:10.1016/j.mex.2019.11.008>) and a WQS with 2 indices (Renzetti et al. (2023) <doi:10.3389/fpubh.2023.1289579>) for continuous, binomial, multinomial, Poisson, quasi-Poisson and negative binomial outcomes.
	"""
	
	cran = "gWQS" 

	version("3.0.5", md5="5c9bec9b9b891ff52f2de3f3ac7f05f0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-plotroc", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-pscl", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-bookdown", type=("build", "run"))
