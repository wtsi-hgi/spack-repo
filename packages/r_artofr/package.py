# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArtofr(RPackage):
	"""To Insert Title, Divider, and Block of Comments

	For instructions, check <https://github.com/Hzhang-ouce/ARTofR>. This is a wrapper of 'bannerCommenter', for inserting neat comments, headers and dividers. 
	"""
	
	cran = "ARTofR" 

	version("0.4.1", md5="cc9f8702d17538fd934d0e6a8ca7dd04")

	depends_on("r-bannercommenter@1:", type=("build", "run"))
	depends_on("r-clipr@0.4:", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
