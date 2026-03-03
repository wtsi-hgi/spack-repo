# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDlsem(RPackage):
	"""Distributed-Lag Linear Structural Equation Models

	Inference functionalities for distributed-lag linear structural equation models (DLSEMs). DLSEMs are Markovian structural causal models where each factor of the joint probability distribution is a distributed-lag linear regression with constrained lag shapes (Magrini, 2018 <doi:10.2478/bile-2018-0012>; Magrini et al., 2019 <doi:10.1007/s11135-019-00855-z>). DLSEMs account for temporal delays in the dependence relationships among the variables through a single parameter per covariate, thus allowing to perform dynamic causal inference in a feasible fashion. Endpoint-constrained quadratic, quadratic decreasing, linearly decreasing and gamma lag shapes are available.
	"""
	
	cran = "dlsem" 

	version("2.4.6", md5="8a4f5d4cc10cffb6fa27811805dd2b0f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
