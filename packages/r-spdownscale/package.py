# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpdownscale(RPackage):
	"""Spatial Downscaling Using Bias Correction Approach

	Spatial downscaling of climate data (Global Circulation Models/Regional Climate Models) using quantile-quantile bias correction technique.
	"""
	
	cran = "spdownscale" 

	version("0.1.0", md5="05264c711c3a87fd866c318dcf7eea55")

	depends_on("r@2.10:", type=("build", "run"))
