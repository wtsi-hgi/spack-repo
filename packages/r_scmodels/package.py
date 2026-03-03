# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScmodels(RPackage):
	"""Fitting Discrete Distribution Models to Count Data

	Provides functions for fitting discrete distribution models to count data.
  Included are the Poisson, the negative binomial, the Poisson-inverse gaussian and, most importantly,
  a new implementation of the Poisson-beta distribution (density, distribution and quantile
  functions, and random number generator) together with a needed new implementation of
  Kummer's function (also: confluent hypergeometric function of the first kind). Three
  different implementations of the Gillespie algorithm allow data simulation based on the
  basic, switching or bursting mRNA generating processes. Moreover, likelihood functions for
  four variants of each of the three aforementioned distributions are also available.
  The variants include one population and two population mixtures, both with and without
  zero-inflation. The package depends on the 'MPFR' libraries (<https://www.mpfr.org/>) which need to be installed separately 
  (see description at <https://github.com/fuchslab/scModels>).
  This package is supplement to the paper "A mechanistic model for the negative binomial distribution of single-cell mRNA counts" 
  by Lisa Amrhein, Kumar Harsha and Christiane Fuchs (2019) <doi:10.1101/657619> available on bioRxiv.
	"""
	
	cran = "scModels" 

	version("1.0.4", md5="047aef0741a54a30fdf69f6903e6b913")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-gamlss-dist", type=("build", "run"))
	depends_on("gmp@4.2.3:", type=("build", "link", "run"))
	depends_on("mpfr@3.0.0:", type=("build", "link", "run"))
