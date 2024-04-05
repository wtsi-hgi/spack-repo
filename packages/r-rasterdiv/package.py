# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRasterdiv(RPackage):
	"""Diversity Indices for Numerical Matrices

	Provides methods to calculate diversity indices on numerical matrices
    based on information theory, as described in Rocchini, Marcantonio and Ricotta (2017) <doi:10.1016/j.ecolind.2016.07.039>,
    and Rocchini et al. (2021) <doi:10.1101/2021.01.23.427872>.
	"""
	
	homepage = "https://mattmar.github.io/rasterdiv/"
	cran = "rasterdiv" 

	version("0.3.4", md5="f746e7e76a523ddbbdef86a8e3323c2f")
	version("0.3.1", md5="b56e6c84d87d6bb8b047ecd9637fb333")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
