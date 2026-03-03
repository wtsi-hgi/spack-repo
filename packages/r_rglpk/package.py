# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRglpk(RPackage):
	"""R/GNU Linear Programming Kit Interface

	R interface to the GNU Linear Programming Kit.
  'GLPK' is open source software for solving large-scale linear programming (LP),
  mixed integer linear programming ('MILP') and other related problems.
	"""
	
	homepage = "https://R-Forge.R-project.org/projects/rglp/"
	cran = "Rglpk" 

	version("0.6-5.1", md5="6531cfc1b0c249fe14524e4fd043bbb1")

	depends_on("r-slam@0.1.9:", type=("build", "run"))
	depends_on("glpk", type=("build", "link", "run"))
