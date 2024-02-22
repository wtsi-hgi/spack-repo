# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class RDiversitree(RPackage):
	"""Comparative 'Phylogenetic' Analyses of Diversification.

	Mostly focusing on analysing diversification and character evolution.
	Contains implementations of 'BiSSE' (Binary State 'Speciation' and
	Extinction) and its unresolved tree extensions, 'MuSSE' (Multiple State
	'Speciation' and Extinction), 'QuaSSE', 'GeoSSE', and 'BiSSE-ness' Other
	included methods include Markov models of discrete and continuous trait
	evolution and constant rate 'speciation' and extinction."""

	cran = "diversitree"

	version("0.10-0", md5="706c67f616f789b0a235b4cc9e5821d9")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-desolve@1.7:", type=("build", "run"))
	depends_on("r-subplex", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("fftw@3.1.2:", type=("build", "link", "run"))
	depends_on("gsl@1.15:", type=("build", "link", "run"))
