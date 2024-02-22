# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultisitemediation(RPackage):
	"""Causal Mediation Analysis in Multisite Trials

	Multisite causal mediation analysis using the methods proposed by Qin and Hong (2017) <doi:10.3102/1076998617694879>, Qin, Hong, Deutsch, and Bein (2019) <doi:10.1111/rssa.12446>, and Qin, Deutsch, and Hong (2021) <doi:10.1002/pam.22268>. It enables causal mediation analysis in multisite trials, in which individuals are assigned to a treatment or a control group at each site. It allows for estimation and hypothesis testing for not only the population average but also the between-site variance of direct and indirect effects transmitted through one single mediator or two concurrent (conditionally independent) mediators. This strategy conveniently relaxes the assumption of no treatment-by-mediator interaction while greatly simplifying the outcome model specification without invoking strong distributional assumptions. This package also provides a function that can further incorporate a sample weight and a nonresponse weight for multisite causal mediation analysis in the presence of complex sample and survey designs and non-random nonresponse, to enhance both the internal validity and external validity. The package also provides a weighting-based balance checking function for assessing the remaining overt bias.
	"""
	
	homepage = "https://github.com/Xu-Qin/MultisiteMediation"
	cran = "MultisiteMediation" 

	version("0.0.4", md5="dfdbde1b54eaf4c876cb3715ce77b710")

	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
