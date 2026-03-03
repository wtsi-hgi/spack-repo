# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCdvinecopulaconditional(RPackage):
	"""Sampling from Conditional C- and D-Vine Copulas

	Provides tools for sampling from a conditional copula density decomposed via 
     Pair-Copula Constructions as C- or D- vine. Here, the vines which can be used for such a 
     sampling are those which sample as first the conditioning variables (when following the 
     sampling algorithms shown in Aas et al. (2009) <DOI:10.1016/j.insmatheco.2007.02.001>). 
     The used sampling algorithm is presented and discussed in Bevacqua et al. (2017) 
     <DOI:10.5194/hess-2016-652>, and it is a modified version of that from Aas et al. (2009) 
     <DOI:10.1016/j.insmatheco.2007.02.001>. A function is available to select the best vine 
     (based on information criteria) among those which allow for such a conditional sampling. 
     The package includes a function to compare scatterplot matrices and pair-dependencies of 
     two multivariate datasets.
	"""
	
	cran = "CDVineCopulaConditional" 

	version("0.1.1", md5="44d337bf9490e574587b9a2f3c272177")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-vinecopula", type=("build", "run"))
