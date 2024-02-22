# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCenscyt(RPackage):
	"""Differential abundance analysis with a right censored covariate in high-dimensional cytometry

	Methods for differential abundance analysis in high-dimensional cytometry data when a covariate is subject to right censoring (e.g. survival time) based on multiple imputation and generalized linear mixed models.
	"""
	
	homepage = "https://github.com/retogerber/censcyt"
	bioc = "censcyt" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/censcyt_1.10.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/censcyt/censcyt_1.10.0.tar.gz"]

	version("1.10.0", md5="e5f2a60dcafc6d878e1e97e85768f078")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-diffcyt", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-broom-mixed", type=("build", "run"))
	depends_on("r-dirmult", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mice", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
