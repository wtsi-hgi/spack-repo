# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTssmoothing(RPackage):
	"""Trend Estimation of Univariate and Bivariate Time Series with
Controlled Smoothness

	It performs the smoothing approach provided by penalized least squares for univariate and bivariate time series, as proposed by Guerrero (2007) and Gerrero et al. (2017). 
          This allows to estimate the time series trend by controlling the amount of resulting (joint) smoothness.
          ---
          Guerrero, V.M (2007)  <DOI:10.1016/j.spl.2007.03.006>.
          Guerrero, V.M; Islas-Camargo, A. and Ramirez-Ramirez, L.L. (2017) <DOI:10.1080/03610926.2015.1133826>.
	"""
	
	cran = "TSsmoothing" 

	version("0.1.0", md5="9f657d1ad08bd29a99b2a54dcd409dc4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.2:", type=("build", "run"))
	depends_on("r-mass@7.3:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-matrix@1.2:", type=("build", "run"))
