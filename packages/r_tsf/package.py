# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsf(RPackage):
	"""Two Stage Forecasting (TSF) for Long Memory Time Series in
Presence of Structural Break

	Forecasting of long memory time series in presence of structural break by using TSF algorithm by Papailias and Dias (2015) <doi:10.1016/j.ijforecast.2015.01.006>. 
	"""
	
	cran = "TSF" 

	version("0.1.1", md5="b16b607a4acfc8921dbd7f04d8914a43")

	depends_on("r-fracdiff", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
