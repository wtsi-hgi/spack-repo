# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBbest(RPackage):
	"""Bayesian Estimation of Incoherent Neutron Scattering Backgrounds

	We implemented a Bayesian-statistics approach for 
        subtraction of incoherent scattering from neutron total-scattering data. 
        In this approach, the estimated background signal associated with 
        incoherent scattering maximizes the posterior probability, which combines 
        the likelihood of this signal in reciprocal and real spaces with the prior 
        that favors smooth lines. The description of the corresponding approach 
        could be found at Gagin and Levin (2014) <DOI:10.1107/S1600576714023796>.
	"""
	
	cran = "BBEST" 

	version("0.1-8", md5="4b398bcb6ff3ad96b6276a7928b5d8af")

	depends_on("r-deoptim", type=("build", "run"))
	depends_on("r-aws", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
