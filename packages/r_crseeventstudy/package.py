# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrseeventstudy(RPackage):
	"""A Robust and Powerful Test of Abnormal Stock Returns in
Long-Horizon Event Studies

	Based on Dutta et al. (2018) <doi:10.1016/j.jempfin.2018.02.004>, this package provides their standardized test for abnormal returns in long-horizon event studies. The methods used improve the major weaknesses of size, power, and robustness of long-run statistical tests described in Kothari/Warner (2007) <doi:10.1016/B978-0-444-53265-7.50015-9>. Abnormal returns are weighted by their statistical precision (i.e., standard deviation), resulting in abnormal standardized returns. This procedure efficiently captures the heteroskedasticity problem. Clustering techniques following Cameron et al. (2011) <doi:10.1198/jbes.2010.07136> are adopted for computing cross-sectional correlation robust standard errors. The statistical tests in this package therefore accounts for potential biases arising from returns' cross-sectional correlation, autocorrelation, and volatility clustering without power loss.
	"""
	
	homepage = "https://github.com/skoestlmeier/crseEventStudy"
	cran = "crseEventStudy" 

	version("1.2.2", md5="4d9fa808dbb2193e9db907fa6e9fc788")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
