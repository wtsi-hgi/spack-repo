# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFracdist(RPackage):
	"""Numerical CDFs for Fractional Unit Root and Cointegration Tests

	Calculate numerical asymptotic distribution functions of likelihood ratio 
    statistics for fractional unit root tests and tests of cointegration rank. 
    For these distributions, the included functions calculate critical values 
    and P-values used in unit root tests, cointegration tests, and rank tests 
    in the Fractionally Cointegrated Vector Autoregression (FCVAR) model.
    The functions implement procedures for tests described in the following articles:
    Johansen, S. and M. Ø. Nielsen (2012) <doi:10.3982/ECTA9299>,
    MacKinnon, J. G. and M. Ø. Nielsen (2014) <doi:10.1002/jae.2295>.
	"""
	
	homepage = "https://github.com/LeeMorinUCF/fracdist"
	cran = "fracdist" 

	version("0.1.1", md5="823ccafea478a048abf7aa85dc44b4f9")

	depends_on("r@2.10:", type=("build", "run"))
