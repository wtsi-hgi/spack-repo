# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGpgp(RPackage):
	"""Fast Gaussian Process Computation Using Vecchia's Approximation

	Functions for fitting and doing predictions with
    Gaussian process models using Vecchia's (1988) approximation. 
    Package also includes functions for reordering input locations, 
    finding ordered nearest neighbors (with help from 'FNN' package), 
    grouping operations, and conditional simulations.
    Covariance functions for spatial and spatial-temporal data
    on Euclidean domains and spheres are provided. The original 
    approximation is due to Vecchia (1988) 
    <http://www.jstor.org/stable/2345768>, and the reordering and
    grouping methods are from Guinness (2018) 
    <doi:10.1080/00401706.2018.1437476>.
    Model fitting employs a Fisher scoring algorithm described
    in Guinness (2019) <arXiv:1905.08374>.
	"""
	
	cran = "GpGp" 

	version("0.5.0", md5="00f6ecf8582b97f686e7a3e5f62135f2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
