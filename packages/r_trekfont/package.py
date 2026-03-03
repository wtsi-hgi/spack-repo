# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrekfont(RPackage):
	"""Star Trek Fonts Collection

	Provides a collection of true type and open type Star Trek-themed fonts.
	"""
	
	homepage = "https://github.com/leonawicz/trekfont"
	cran = "trekfont" 

	version("0.9.5", md5="22c3ed81f6428b30c14c51317c867ff4")

	depends_on("r@2.10:", type=("build", "run"))
