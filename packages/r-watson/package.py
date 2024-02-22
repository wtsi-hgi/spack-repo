# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWatson(RPackage):
	"""Fitting and Simulating Mixtures of Watson Distributions

	Tools for fitting and simulating mixtures of Watson distributions. 
             The random sampling scheme of the package offers two sampling 
             algorithms that are based of the results of Sablica, Hornik and Leydold (2022)
             <https://research.wu.ac.at/en/publications/random-sampling-from-the-watson-distribution>.
             What is more, the package offers a smart tool to combine these two methods,
             and based on the selected parameters, it approximates the relative sampling
             speed for both methods and picks the faster one. In addition, the package
             offers a fitting function for the mixtures of Watson distribution, that
             uses the expectation-maximization (EM) algorithm. Special features are
             the possibility to use multiple variants of the E-step and M-step,
             sparse matrices for the data representation and state of the art methods
             for numerical evaluation of needed special functions using the results of
             Sablica and Hornik (2022) <https://www.ams.org/journals/mcom/2022-91-334/S0025-5718-2021-03690-X/>.
	"""
	
	cran = "watson" 

	version("0.4", md5="a70c8089d5a47b418da96f94952b19f3")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-tinflex", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
