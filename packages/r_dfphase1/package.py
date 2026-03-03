# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDfphase1(RPackage):
	"""Phase I Control Charts (with Emphasis on Distribution-Free
Methods)

	Statistical methods for retrospectively detecting changes
             in location and/or dispersion of univariate and multivariate 
             variables. Data values are assumed to be independent, can be 
             individual (one observation at each instant of time) or subgrouped 
             (more than one observation at each instant of time). 
             Control limits are computed, often using a permutation approach, 
             so that a prescribed false alarm probability is guaranteed  
             without making any parametric assumptions on the stable 
             (in-control) distribution. See G. Capizzi and G. Masarotto (2018) 
             <doi:10.1007/978-3-319-75295-2_1> for an introduction to the package.
	"""
	
	cran = "dfphase1" 

	version("1.2.0", md5="9c0dbc223ade3a3d72d6fc66f7a76360", url="https://cran.r-project.org/src/contrib/dfphase1_1.2.0.tar.gz")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
