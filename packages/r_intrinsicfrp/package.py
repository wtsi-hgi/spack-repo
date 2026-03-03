# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntrinsicfrp(RPackage):
	"""An R Package for Factor Model Asset Pricing

	Functions for evaluating and testing asset pricing models, including
    estimation and testing of factor risk premia, selection of "strong" risk 
    factors (factors having nonzero population correlation with test asset
    returns), heteroskedasticity and autocorrelation robust covariance matrix
    estimation and testing for model misspecification and identification. 
    The functions for estimating and testing factor risk 
    premia implement the Fama-MachBeth (1973) <doi:10.1086/260061> two-pass 
    approach, the misspecification-robust approaches of Kan-Robotti-Shanken (2013) 
    <doi:10.1111/jofi.12035>, and the approaches based on tradable factor risk
    premia of Quaini-Trojani-Yuan (2023) <doi:10.2139/ssrn.4574683>. The 
    functions for selecting the "strong" risk factors are based on the Oracle
    estimator of Quaini-Trojani-Yuan (2023) <doi:10.2139/ssrn.4574683> and the 
    factor screening procedure of Gospodinov-Kan-Robotti (2014) <doi:10.2139/ssrn.2579821>. 
    The functions for evaluating model misspecification implement the HJ
    model misspecification distance of Kan-Robotti (2008) <doi:10.1016/j.jempfin.2008.03.003>,
    which is a modification of the prominent Hansen-Jagannathan (1997)
    <doi:10.1111/j.1540-6261.1997.tb04813.x> distance.
    The functions for testing model identification 
    specialize the Kleibergen-Paap (2006) <doi:10.1016/j.jeconom.2005.02.011> 
    and the Chen-Fang (2019) <doi:10.1111/j.1540-6261.1997.tb04813.x> rank test 
    to the regression coefficient matrix of test asset returns on risk factors.
    Finally, the function for heteroskedasticity and autocorrelation robust 
    covariance estimation implements the Newey-West (1994) <doi:10.2307/2297912>
    covariance estimator.
	"""
	
	homepage = "https://github.com/a91quaini/intrinsicFRP"
	cran = "intrinsicFRP" 

	version("2.0.1", md5="783a685a63e889468222396d136fb766")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
