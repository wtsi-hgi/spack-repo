# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVewaningvariant(RPackage):
	"""Vaccine Efficacy Over Time - Variant Aware

	Implements methods for inference on potential waning of vaccine efficacy and for estimation of vaccine efficacy at a user-specified time after vaccination based on data from a randomized, double-blind, placebo-controlled vaccine trial in which participants may be unblinded and placebo subjects may be crossed over to the study vaccine.  The methods also for variant stratification and allow adjustment for possible confounding via inverse probability weighting through specification of models for the trial entry process, unblinding mechanisms, and the probability an unblinded placebo participant accepts study vaccine.
	"""
	
	cran = "VEwaningVariant" 

	version("1.4", md5="cf4f68e3a6c49f30c946f1adbe11e331")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
