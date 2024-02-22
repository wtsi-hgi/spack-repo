# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBacct(RPackage):
	"""Bayesian Augmented Control for Clinical Trials

	Implements the Bayesian Augmented Control (BAC, a.k.a. Bayesian historical data borrowing) method under clinical trial setting by calling 'Just Another Gibbs Sampler' ('JAGS') software. In addition, the 'BACCT' package evaluates user-specified decision rules by computing the type-I error/power, or probability of correct go/no-go decision at interim look. The evaluation can be presented numerically or graphically. Users need to have 'JAGS' 4.0.0 or newer installed due to a compatibility issue with 'rjags' package. Currently, the package implements the BAC method for binary outcome only. Support for continuous and survival endpoints will be added in future releases. We would like to thank AbbVie's Statistical Innovation group and Clinical Statistics group for their support in developing the 'BACCT' package.
	"""
	
	cran = "BACCT" 

	version("1.0", md5="3af2fc744feb63b57019478a76f513c4")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
