# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsce(RPackage):
	"""Hazard of Multi-Stage Clonal Expansion Models

	Functions to calculate hazard and survival function of Multi-Stage Clonal Expansion Models used in cancer epidemiology. For the Two-Stage Clonal Expansion Model an exact solution is implemented assuming piecewise constant parameters. Numerical solutions are provided for its extensions.
	"""
	
	cran = "msce" 

	version("1.0.1", md5="0f89be7c20c5a0799e90793ac4ae7699")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
