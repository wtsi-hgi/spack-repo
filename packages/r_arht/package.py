# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArht(RPackage):
	"""Adaptable Regularized Hotelling's T^2 Test for High-Dimensional
Data

	Perform the Adaptable Regularized Hotelling's T^2 test (ARHT) proposed by
    Li et al., (2016) <arXiv:1609.08725>. Both one-sample and two-sample mean test are available with
    various probabilistic alternative prior models. It contains a function to consistently
    estimate higher order moments of the population covariance spectral distribution using
    the spectral of the sample covariance matrix (Bai et al. (2010) <doi:10.1111/j.1467-842X.2010.00590.x>).
    In addition, it contains a function to sample from 3-variate chi-squared random vectors approximately 
    with a given correlation matrix when the degrees of freedom are large. 
	"""
	
	cran = "ARHT" 

	version("0.1.0", md5="44cbf0c77d4d719441bece5920c0b01d")

	depends_on("r@2.10:", type=("build", "run"))
