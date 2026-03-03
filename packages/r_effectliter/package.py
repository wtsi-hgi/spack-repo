# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REffectliter(RPackage):
	"""Average and Conditional Effects

	Use structural equation modeling to estimate average and
    conditional effects of a treatment variable on an outcome variable, taking into
    account multiple continuous and categorical covariates.
	"""
	
	homepage = "https://github.com/amayer2010/EffectLiteR"
	cran = "EffectLiteR" 

	version("0.4-6", md5="69179e8ee1a7105addc51bef4f9b18b7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lavaan@0.6.8:", type=("build", "run"))
	depends_on("r-shiny@1.5:", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
