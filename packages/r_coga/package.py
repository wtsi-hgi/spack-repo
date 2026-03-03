# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoga(RPackage):
	"""Convolution of Gamma Distributions

	Evaluation for density and distribution function of convolution of gamma
    distributions in R. Two related exact methods and one approximate method are
    implemented with efficient algorithm and C++ code. A quick guide for choosing
    correct method and usage of this package is given in package vignette. For the
    detail of methods used in this package, we refer the user to
    Mathai(1982)<doi:10.1007/BF02481056>,
    Moschopoulos(1984)<doi:10.1007/BF02481123>,
    Barnabani(2017)<doi:10.1080/03610918.2014.963612>,
    Hu et al.(2020)<doi:10.1007/s00180-019-00924-9>.
	"""
	
	homepage = "https://github.com/ChaoranHu/coga"
	cran = "coga" 

	version("1.2.2", md5="df4b2c0de5960141d6e0b6e7c56217ff")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
	depends_on("r-rcppgsl", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
