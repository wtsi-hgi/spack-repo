# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrddisp(RPackage):
	"""Separating Location and Dispersion in Ordinal Regression Models

	Estimate location-shift models or rating-scale models accounting for response styles (RSRS) for the regression analysis of ordinal responses.
	"""
	
	cran = "ordDisp" 

	version("2.1.1", md5="fe8a7697fd2cf788e5f7643f77993e2b")

	depends_on("r-vgam", type=("build", "run"))
