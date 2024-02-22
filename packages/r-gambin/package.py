# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGambin(RPackage):
	"""Fit the Gambin Model to Species Abundance Distributions

	Fits unimodal and multimodal gambin distributions to species-abundance distributions
    from ecological data, as in in Matthews et al. (2014) <DOI:10.1111/ecog.00861>. 
    'gambin' is short for 'gamma-binomial'. The main function is fit_abundances(), which estimates 
    the 'alpha' parameter(s) of the gambin distribution using maximum likelihood. Functions are 
    also provided to generate the gambin distribution and for calculating likelihood statistics.
	"""
	
	homepage = "https://github.com/txm676/gambin/"
	cran = "gambin" 

	version("2.5.0", md5="1f183a430c8a09daf691657bf2b3a71d")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
