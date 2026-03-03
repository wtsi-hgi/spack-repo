# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvnormaltest(RPackage):
	"""Powerful Tests for Multivariate Normality

	A simple informative powerful test (mvnTest()) for multivariate normality proposed by 
    Zhou and Shao (2014) <doi:10.1080/02664763.2013.839637>, which combines kurtosis 
    with Shapiro-Wilk test that is easy for biomedical researchers to understand and 
    easy to implement in all dimensions. This package also contains some other multivariate 
    normality tests including Fattorini's FA test (faTest()), Mardia's skewness and kurtosis 
    test (mardia()), Henze-Zirkler's test (mhz()), Bowman and Shenton's test (msk()), 
    Royston’s H test (msw()), and Villasenor-Alva and Gonzalez-Estrada's test (msw()). Empirical 
    power calculation functions for these tests are also provided. In addition, this package 
    includes some functions to generate several types of multivariate distributions mentioned in 
    Zhou and Shao (2014).
	"""
	
	cran = "mvnormalTest" 

	version("1.0.0", md5="f3525fd9bd8d908ba0b2201a3f147039")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-nortest", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
