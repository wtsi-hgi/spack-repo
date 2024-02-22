# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMob(RPackage):
	"""Monotonic Optimal Binning

	Generate the monotonic binning and
    perform the woe (weight of evidence) transformation for the logistic regression
    used in the consumer credit scorecard development. The woe transformation is a piecewise
    transformation that is linear to the log odds. For a numeric variable, all of its monotonic 
    functional transformations will converge to the same woe transformation. 
	"""
	
	homepage = "https://github.com/statcompute/mob"
	cran = "mob" 

	version("0.4.2", md5="2470876384a4c092f5a853ad25b51961")

	depends_on("r@3.3.3:", type=("build", "run"))
	depends_on("r-gbm", type=("build", "run"))
	depends_on("r-rborist", type=("build", "run"))
