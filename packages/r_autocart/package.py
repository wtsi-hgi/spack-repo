# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAutocart(RPackage):
	"""Autocorrelation Regression Trees

	A modified version of the classification and regression tree (CART) 
    algorithm for modelling spatial data that features coordinate information.
    Coordinate information can be used to evaluate measures of spatial
    autocorrelation and spatial compactness during the splitting phase of the
    tree, leading to better predictions and more physically realistic predictions
    on these types of datasets. These methods are described in Ancell and Bean (2021)
    <arXiv:2101.08258>.
	"""
	
	cran = "autocart" 

	version("1.4.5", md5="dba5077f923e0f0a1e9fd480d3913c85")

	depends_on("r-fields", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
