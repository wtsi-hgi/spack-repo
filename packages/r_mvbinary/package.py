# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvbinary(RPackage):
	"""Modelling Multivariate Binary Data with Blocks of Specific
One-Factor Distribution

	Modelling Multivariate Binary Data with Blocks of Specific One-Factor Distribution. Variables are grouped into independent blocks. Each variable is described by two continuous parameters (its marginal probability and its dependency strength with the other block variables), and one binary parameter (positive or negative dependency). Model selection consists in the estimation of the repartition of the variables into blocks. It is carried out by the maximization of the BIC criterion by a deterministic (faster) algorithm or by a stochastic (more time consuming but optimal) algorithm. Tool functions facilitate the model interpretation.
	"""
	
	cran = "MvBinary" 

	version("1.1", md5="b667694486e9768d8c0c1f1f52bcdb7c")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
