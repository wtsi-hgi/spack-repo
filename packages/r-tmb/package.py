# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTmb(RPackage):
	"""Template Model Builder: A General Random Effect Tool Inspired by
'ADMB'

	With this tool, a user should be able to quickly implement
    complex random effect models through simple C++ templates. The package combines
    'CppAD' (C++ automatic differentiation), 'Eigen' (templated matrix-vector
    library) and 'CHOLMOD' (sparse matrix routines available from R) to obtain
    an efficient implementation of the applied Laplace approximation with exact
    derivatives. Key features are: Automatic sparseness detection, parallelism
    through 'BLAS' and parallel user templates.
	"""
	
	homepage = "https://github.com/kaskr/adcomp/wiki"
	cran = "TMB" 

	version("1.9.10", md5="6554e07819b6fc786df8d68a19733344")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
