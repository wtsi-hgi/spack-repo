# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTcomp(RPackage):
	"""Data from the 2010 Tourism Forecasting Competition

	The 1311 time series from the tourism forecasting competition conducted in 2010 and described in Athanasopoulos et al. (2011) <DOI:10.1016/j.ijforecast.2010.04.009>.
	"""
	
	cran = "Tcomp" 

	version("1.0.1", md5="8dd69a1f0ef244979e36a94f9905527c")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-mcomp", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
