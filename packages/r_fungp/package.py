# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFungp(RPackage):
	"""Gaussian Process Models for Scalar and Functional Inputs

	Construction and smart selection of Gaussian process models
	for analysis of computer experiments
	with emphasis on treatment of functional inputs that are regularly sampled. This package
	offers: (i) flexible modeling of functional-input regression
	problems through the fairly general Gaussian process model; (ii)
	built-in dimension reduction for functional inputs; (iii)
	heuristic optimization of the structural parameters of the model
	(e.g., active inputs, kernel function, type of distance).
	Metamodeling background is provided in
	Betancourt et al. (2020) <doi:10.1016/j.ress.2020.106870>.
	The algorithm for structural parameter optimization is described
	in <https://hal.archives-ouvertes.fr/hal-02532713>.
	"""
	
	homepage = "https://djbetancourt-gh.github.io/funGp/"
	cran = "funGp" 

	version("0.3.2", md5="5c451208239964bd6e5639a939f2d1a2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-microbenchmark", type=("build", "run"))
	depends_on("r-dofuture", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
