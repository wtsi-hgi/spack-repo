# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGamrr(RPackage):
	"""Calculate the RR for the GAM

	To calculate the relative risk (RR) for the generalized additive model.
	"""
	
	cran = "gamRR" 

	version("0.7.0", md5="f9fe20f553bfe61d6a6d520818167b00")

	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
