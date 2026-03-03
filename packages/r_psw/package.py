# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsw(RPackage):
	"""Propensity Score Weighting Methods for Dichotomous Treatments

	Provides propensity score weighting methods to control for confounding in causal inference with dichotomous treatments and continuous/binary outcomes. It includes the following functional modules: (1) visualization of the propensity score distribution in both treatment groups with mirror histogram, (2) covariate balance diagnosis, (3) propensity score model specification test, (4) weighted estimation of treatment effect, and (5) augmented estimation of treatment effect with outcome regression. The weighting methods include the inverse probability weight (IPW) for estimating the average treatment effect (ATE), the IPW for average treatment effect of the treated (ATT), the IPW for the average treatment effect of the controls (ATC), the matching weight (MW), the overlap weight (OVERLAP), and the trapezoidal weight (TRAPEZOIDAL). Sandwich variance estimation is provided to adjust for the sampling variability of the estimated propensity score. These methods are discussed by Hirano et al (2003) <DOI:10.1111/1468-0262.00442>, Lunceford and Davidian (2004) <DOI:10.1002/sim.1903>, Li and Greene (2013) <DOI:10.1515/ijb-2012-0030>, and Li et al (2016) <DOI:10.1080/01621459.2016.1260466>.
	"""
	
	cran = "PSW" 

	version("1.1-3", md5="82d74e475539df2ed6f8a0156cc7061f")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
