# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntkrige(RPackage):
	"""A Numerical Implementation of Interval-Valued Kriging

	An interval-valued extension of ordinary and simple kriging.
    Optimization of the function is based on a generalized interval distance.
    This creates a non-differentiable cost function that requires a
    differentiable approximation to the absolute value function. This
    differentiable approximation is optimized using a Newton-Raphson algorithm
    with a penalty function to impose the constraints. Analyses in the package
    are driven by the 'intsp' and 'intgrd' 
    classes, 
    which are interval-valued extensions of
    'SpatialPointsDataFrame' and 'SpatialPixelsDataFrame' respectively. 
    The package includes several wrappers to functions in the 
    'gstat' and 'sp' packages.
	"""
	
	cran = "intkrige" 

	version("1.0.1", md5="6d3f98448be99ba24204927795ed7d78")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sp@1.3.1:", type=("build", "run"))
	depends_on("r-gstat", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
