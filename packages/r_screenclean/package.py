# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScreenclean(RPackage):
	"""Screen and clean variable selection procedures

	Routines for a collection of screen-and-clean type
        variable selection procedures, including UPS and GS.
	"""
	
	cran = "ScreenClean" 

	version("1.0.1", md5="e2d82fa5357a6b2a823b06252ae9a168")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
