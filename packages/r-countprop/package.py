# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCountprop(RPackage):
	"""Calculate Model-Based Metrics of Proportionality on Count-Based
Compositional Data

	Calculates metrics of proportionality using the logit-normal multinomial model.  It can also provide empirical and plugin estimates of these metrics.
	"""
	
	cran = "countprop" 

	version("1.0.1", md5="5fa14218784585c346cfcc540f2c6714")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-glasso", type=("build", "run"))
	depends_on("r-compositions", type=("build", "run"))
	depends_on("r-zcompositions", type=("build", "run"))
