# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCodyn(RPackage):
	"""Community Dynamics Metrics

	Univariate and multivariate temporal and spatial diversity indices, 
    rank abundance curves, and community stability measures. The functions 
    implement measures that are either explicitly temporal and include the 
    option to calculate them over multiple replicates, or spatial and include 
    the option to calculate them over multiple time points. Functions fall into 
    five categories: static diversity indices, temporal diversity indices, 
    spatial diversity indices, rank abundance curves, and community stability 
    measures. The diversity indices are temporal and spatial analogs to 
    traditional diversity indices. Specifically, the package includes functions 
    to calculate community richness, evenness and diversity at a given point in 
    space and time. In addition, it contains functions to calculate species 
    turnover, mean rank shifts, and lags in community similarity between two 
    time points. Details of the methods are available in
    Hallett et al. (2016) <doi:10.1111/2041-210X.12569> and Avolio 
    et al. (2019) <doi:10.1002/ecs2.2881>.
	"""
	
	homepage = "https://github.com/NCEAS/codyn/"
	cran = "codyn" 

	version("2.0.5", md5="3bc95fc99ad267d2152e9c550527024e")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-permute", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
