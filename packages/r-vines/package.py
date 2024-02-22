# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVines(RPackage):
	"""Multivariate Dependence Modeling with Vines

	Implementation of the vine graphical model for building
    high-dimensional probability distributions as a factorization of
    bivariate copulas and marginal density functions. This package
    provides S4 classes for vines (C-vines and D-vines) and methods
    for inference, goodness-of-fit tests, density/distribution
    function evaluation, and simulation.
	"""
	
	homepage = "https://github.com/yasserglez/vines"
	cran = "vines" 

	version("1.1.5", md5="ca1ca64ac6c625d89d2ab7c6809f2984")

	depends_on("r-copula", type=("build", "run"))
	depends_on("r-adgoftest", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
	depends_on("r-tsp", type=("build", "run"))
