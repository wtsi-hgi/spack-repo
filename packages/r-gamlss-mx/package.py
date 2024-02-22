# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGamlssMx(RPackage):
	"""Fitting Mixture Distributions with GAMLSS

	The main purpose of this package is to allow fitting of
        mixture distributions with generalised additive models for location 
        scale and shape models see Chapter 7 of Stasinopoulos et al. (2017) <doi:10.1201/b21973-4>.
	"""
	
	homepage = "https://www.gamlss.com/"
	cran = "gamlss.mx" 

	version("6.0-1", md5="2d63fe32e59908437daa51c040b5fc26")

	depends_on("r@2.2.1:", type=("build", "run"))
	depends_on("r-gamlss-dist", type=("build", "run"))
	depends_on("r-gamlss", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
