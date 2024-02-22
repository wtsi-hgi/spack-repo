# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsycmodel(RPackage):
	"""Integrated Toolkit for Psychological Analysis and Modeling in R

	A beginner-friendly R package for modeling in psychology or
    related field. It allows fitting models, plotting, checking goodness
    of fit, and model assumption violations all in one place. It also
    produces beautiful and easy-to-read output.
	"""
	
	homepage = "https://github.com/jasonmoy28/psycModel"
	cran = "psycModel" 

	version("0.5.0", md5="837e16ff3a6d03f715fe768fb2c9fdcf")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-insight", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
	depends_on("r-parameters", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-performance", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-rlang@0.1.2:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
