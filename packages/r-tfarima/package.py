# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTfarima(RPackage):
	"""Transfer Function and ARIMA Models

	Building customized transfer function and ARIMA models with multiple operators and parameter restrictions. Functions for model identification, model estimation (exact or conditional maximum likelihood), model diagnostic checking, automatic outlier detection, calendar effects, forecasting and seasonal adjustment. See Bell and Hillmer (1983) <doi:10.1080/01621459.1983.10478005>, Box, Jenkins, Reinsel and Ljung <ISBN:978-1-118-67502-1>, Box, Pierce and Newbold (1987) <doi:10.1080/01621459.1987.10478430>, Box and Tiao (1975) <doi:10.1080/01621459.1975.10480264>, Chen and Liu (1993) <doi:10.1080/01621459.1993.10594321>.
	"""
	
	homepage = "https://github.com/gallegoj/tfarima"
	cran = "tfarima" 

	version("0.3.2", md5="29cc9ff5bc513f5af8eea64382adca29")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
