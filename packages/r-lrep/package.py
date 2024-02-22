# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLrep(RPackage):
	"""Estimate and Test Exponential vs. Pareto Distributions

	The programs were developed for estimation of parameters and testing exponential versus Pareto distribution during our work on hydrologic extremes. See Kozubowski, T.J., A.K. Panorska, F. Qeadan, and A. Gershunov (2007) <doi:10.1080/03610910802439121>, and Panorska, A.K., A. Gershunov, and T.J. Kozubowski (2007) <doi:10.1007/978-0-387-34918-3_26>.
	"""
	
	cran = "LREP" 

	version("0.1.1", md5="16082b993da77d08a30429a8858d02fb")

	depends_on("r@4:", type=("build", "run"))
