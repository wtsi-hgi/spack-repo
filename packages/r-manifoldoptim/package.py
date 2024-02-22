# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RManifoldoptim(RPackage):
	"""An R Interface to the 'ROPTLIB' Library for Riemannian Manifold
Optimization

	An R interface to version 0.3 of the 'ROPTLIB' optimization library
    (see <https://www.math.fsu.edu/~whuang2/> for more information). Optimize real-
    valued functions over manifolds such as Stiefel, Grassmann, and Symmetric
    Positive Definite matrices. For details see Martin et. al. (2020) <doi:10.18637/jss.v093.i01>. 
    Note that the optional ldr package used in some of this package's examples can be obtained from either JSS 
    <https://www.jstatsoft.org/index.php/jss/article/view/v061i03/2886> or from the CRAN archives 
    <https://cran.r-project.org/src/contrib/Archive/ldr/ldr_1.3.3.tar.gz>.
	"""
	
	cran = "ManifoldOptim" 

	version("1.0.1", md5="33b550a63b13853385ddd05261982f20")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
