# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTablemonster(RPackage):
	"""Table Monster

	Provides a user friendly interface to 
  generation of booktab style tables using 'xtable'. 
	"""
	
	homepage = "<https://www.youtube.com/watch?v=CM1TaNVnh58>"
	cran = "TableMonster" 

	version("1.7", md5="ed54f84acde6ea67037e403b523a35fd")

	depends_on("r-xtable", type=("build", "run"))
