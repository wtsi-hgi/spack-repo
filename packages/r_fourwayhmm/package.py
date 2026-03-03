# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFourwayhmm(RPackage):
	"""Parsimonious Hidden Markov Models for Four-Way Data

	Implements parsimonious hidden Markov models for four-way data via expectation-
    conditional maximization algorithm, as described in Tomarchio et al. (2020) <arXiv:2107.04330>.
    The matrix-variate normal distribution is used as emission distribution. For each hidden
    state, parsimony is reached via the eigen-decomposition of the covariance matrices of the
    emission distribution. This produces a family of 98 parsimonious hidden Markov models.
	"""
	
	cran = "FourWayHMM" 

	version("1.0.0", md5="1cd4298afb8b62d9ae331e7e246fe01f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-snow", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-tensor", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-laplacesdemon", type=("build", "run"))
