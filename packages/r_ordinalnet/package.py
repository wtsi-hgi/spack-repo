# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrdinalnet(RPackage):
	"""Penalized Ordinal Regression

	Fits ordinal regression models with elastic net penalty.
    Supported model families include cumulative probability, stopping ratio, 
    continuation ratio, and adjacent category. These families are a subset of 
    vector glm's which belong to a model class we call the elementwise link 
    multinomial-ordinal (ELMO) class. Each family in this class links a vector 
    of covariates to a vector of class probabilities. Each of these families 
    has a parallel form, which is appropriate for ordinal response data, as 
    well as a nonparallel form that is appropriate for an unordered categorical
    response, or as a more flexible model for ordinal data. The parallel model
    has a single set of coefficients, whereas the nonparallel model has a set of
    coefficients for each response category except the baseline category. It is 
    also possible to fit a model with both parallel and nonparallel terms, which 
    we call the semi-parallel model. The semi-parallel model has the flexibility 
    of the nonparallel model, but the elastic net penalty shrinks it toward the 
    parallel model. For details, refer to Wurm, Hanlon, and Rathouz (2021) 
    <doi:10.18637/jss.v099.i06>.
	"""
	
	cran = "ordinalNet" 

	version("2.12", md5="7c5bf3423a4bab90dd61f62ed82c8403")

