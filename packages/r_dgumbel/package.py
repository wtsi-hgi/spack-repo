# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDgumbel(RPackage):
	"""The Gumbel Distribution Functions and Gradients

	Gumbel distribution functions (De Haan L. (2007)
    <doi:10.1007/0-387-34471-3>) implemented with the techniques of automatic
    differentiation (Griewank A. (2008) <isbn:978-0-89871-659-7>).
    With this tool, a user should be able to quickly model extreme
    events for which the Gumbel distribution is the domain of attraction.
    The package makes available the density function, the distribution
    function the quantile function and a random generating function. In
    addition, it supports gradient functions. The package combines 'Adept'
    (C++ templated automatic differentiation) (Hogan R. (2017)
    <doi:10.5281/zenodo.1004730>) and 'Eigen' (templated matrix-vector
    library) for fast computations of both objective functions and exact
    gradients. It relies on 'RcppEigen' for easy access to 'Eigen' and
    bindings to R.
	"""
	
	homepage = "https://github.com/blunde1/dgumbel"
	cran = "dgumbel" 

	version("1.0.1", md5="3650e3cf19180abd0fe2ab2432fe1bb4")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
