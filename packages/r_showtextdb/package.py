# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShowtextdb(RPackage):
	"""Font Files for the 'showtext' Package

	Providing font files that can be used by the 'showtext' package.
	"""
	
	cran = "showtextdb" 

	version("3.0", md5="f70b8177f5cd2805148bf01822ed2c19")

	depends_on("r-sysfonts@0.7:", type=("build", "run"))
