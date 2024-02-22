# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSei(RPackage):
	"""Calculating Standardised Indices

	Convert a time series of observations to a time series of standardised indices that can be used to monitor variables on a common and probabilistically interpretable scale. The indices can be aggregated and rescaled to different time scales, visualised using plot capabilities, and calculated using a range of distributions. This includes flexible non- and semi-parametric methods, as suggested by Allen and Otero (2023) <doi:10.1016/j.renene.2023.119206>.
	"""
	
	homepage = "https://github.com/noeliaof/SEI"
	cran = "SEI" 

	version("0.1.1", md5="12e13af24ff4076a02f148c48ac05942")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
