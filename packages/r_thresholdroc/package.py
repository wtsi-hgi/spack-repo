# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RThresholdroc(RPackage):
	"""Optimum Threshold Estimation

	Functions that provide point and interval estimations of optimum thresholds for continuous diagnostic tests. The methodology used is based on minimizing an overall cost function in the two- and three-state settings. We also provide functions for sample size determination and estimation of diagnostic accuracy measures. We also include graphical tools. The statistical methodology used here can be found in Perez-Jaume et al (2017) <doi:10.18637/jss.v082.i04> and in Skaltsa et al (2010, 2012) <doi:10.1002/bimj.200900294>, <doi:10.1002/sim.4369>.
	"""
	
	cran = "ThresholdROC" 

	version("2.9.3", md5="4db24d93c051413766006b187b3d5a5f")
	version("2.9.2", md5="750ec842d40c40e2e883169aaab80369")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
