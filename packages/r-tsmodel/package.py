# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsmodel(RPackage):
	"""Time Series Modeling for Air Pollution and Health

	Tools for specifying time series regression models.
	"""
	
	cran = "tsModel" 

	version("0.6-1", md5="b7644990d30db65e6d614679efaf1aea")

	depends_on("r@4:", type=("build", "run"))
