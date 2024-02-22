# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmerconveniencefunctions(RPackage):
	"""Model Selection and Post-Hoc Analysis for (G)LMER Models

	The main function of the package is to perform backward selection of fixed effects, forward fitting of the random effects, and post-hoc analysis using parallel capabilities. Other functionality includes the computation of ANOVAs with upper- or lower-bound p-values and R-squared values for each model term, model criticism plots, data trimming on model residuals, and data visualization. The data to run examples is contained in package LCF_data.
	"""
	
	cran = "LMERConvenienceFunctions" 

	version("3.0", md5="46b507baa946ea7c2b280baad4467428")

	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-lcfdata", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
