# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RThestats(RPackage):
	"""R Package for Exploring Turkish Higher Education Statistics

	A user-friendly R data package that is intended to make Turkish higher education statistics more accessible. 
	"""
	
	homepage = "https://github.com/analyticsresearchlab/thestats"
	cran = "thestats" 

	version("0.1.0", md5="cf41eb21cbf2d12d7f31970501ca931f")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-dplyr@1.0.6:", type=("build", "run"))
