# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptimaldesign(RPackage):
	"""A Toolbox for Computing Efficient Designs of Experiments

	Algorithms for D-, A-, I-, and c-optimal designs. Some of the functions in this package require the 'gurobi' software and its accompanying R package. For their installation, please follow the instructions at <https://www.gurobi.com> and the file gurobi_inst.txt, respectively.
	"""
	
	homepage = "<"
	cran = "OptimalDesign" 

	version("1.0.1", md5="84f6e5fb5a15ece6e190e449c8e3f238")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
