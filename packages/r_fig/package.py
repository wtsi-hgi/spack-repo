# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFig(RPackage):
	"""A Config Package with No "Con"

	Work with configs with a source precedence. Either create own R6
  instance or work with convenient functions at a package level.
	"""
	
	homepage = "https://github.com/TymekDev/fig"
	cran = "fig" 

	version("1.0.0", md5="bd22d803ae598cc7b759c278f59a0cb5")

	depends_on("r-r6", type=("build", "run"))
