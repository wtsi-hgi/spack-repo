# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoiPluginCplex(RPackage):
	"""ROI Plug-in CPLEX

	Enhances the R Optimization Infrastructure (ROI) package by registering
	     the 'CPLEX' commercial solver. It allows for solving mixed integer quadratically
	     constrained programming (MIQPQC) problems as well as all
	     variants/combinations of LP, QP, QCP, IP.
	"""
	
	homepage = "http://R-Forge.R-project.org/projects/roi"
	cran = "ROI.plugin.cplex" 

	version("0.3-0", md5="fbc4ab1981668bb0fd35aaa7c0521063")

	depends_on("r-roi@0.3.0:", type=("build", "run"))
	depends_on("r-rcplex@0.3.3:", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
