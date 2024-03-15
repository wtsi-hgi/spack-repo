# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class RRrpp(RPackage):
	"""Linear Model Evaluation with Randomized Residuals in a Permutation
	Procedure.

	Linear model calculations are made for many random versions of data. Using
	residual randomization in a permutation procedure, sums of squares are
	calculated over many permutations to generate empirical probability
	distributions for evaluating model effects. This packaged is described by
	Collyer & Adams (2018) <doi:10.1111/2041-210X.13029>. Additionally,
	coefficients, statistics, fitted values, and residuals generated over many
	permutations can be used for various procedures including pairwise tests,
	prediction, classification, and model comparison. This package should
	provide most tools one could need for the analysis of high-dimensional
	data, especially in ecology and evolutionary biology, but certainly other
	fields, as well."""

	cran = "RRPP"

	version("2.0.0", md5="d434418b16fe09fb649960570aed88c1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
