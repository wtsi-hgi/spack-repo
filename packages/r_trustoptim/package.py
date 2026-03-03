# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrustoptim(RPackage):
	"""Trust Region Optimization for Nonlinear Functions with Sparse
Hessians

	Trust region algorithm for nonlinear optimization. Efficient when
    the Hessian of the objective function is sparse (i.e., relatively few nonzero
    cross-partial derivatives). See Braun, M. (2014) <doi:10.18637/jss.v060.i04>.
	"""
	
	homepage = "https://braunm.github.io/trustOptim/"
	cran = "trustOptim" 

	version("0.8.7.3", md5="939e983ceff654c5efcf326cf5ee67a7")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-matrix@1.2.18:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.7:", type=("build", "run"))
