# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCgnm(RPackage):
	"""Cluster Gauss-Newton Method

	Find multiple solutions of a nonlinear least squares problem.  Cluster Gauss-Newton method does not assume uniqueness of the solution of the nonlinear least squares problem and compute multiple minimizers. Please cite the following paper when this software is used in your research: Aoki et al. (2020) <doi:10.1007/s11081-020-09571-2>. Cluster Gauss–Newton method. Optimization and Engineering, 1-31.  Please cite the following paper when profile likelihood plot is drawn with this software and used in your research: Aoki and Sugiyama (2024) <doi:10.1002/psp4.13055>. Cluster Gauss-Newton method for a quick approximation of profile likelihood: With application to physiologically-based pharmacokinetic models. CPT Pharmacometrics Syst Pharmacol.13(1):54-67. 
	"""
	
	cran = "CGNM" 

	version("0.6.7", md5="b687b21c1c0dba105d8b7ce0f2c5b1d5")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
