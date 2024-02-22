# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoptim(RPackage):
	"""General Purpose Optimization in R using C++

	Perform general purpose optimization in R using C++. A unified 
    wrapper interface is provided to call C functions of the five optimization 
    algorithms ('Nelder-Mead', 'BFGS', 'CG', 'L-BFGS-B' and 'SANN') underlying 
    optim().
	"""
	
	homepage = "https://github.com/ypan1988/roptim/"
	cran = "roptim" 

	version("0.1.6", md5="70829db206696b734533a84ade4619cb")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
