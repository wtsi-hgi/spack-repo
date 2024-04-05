# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWavscalogram(RPackage):
	"""Wavelet Scalogram Tools for Time Series Analysis

	Provides scalogram based wavelet tools for time series analysis: wavelet power spectrum, scalogram, windowed scalogram, windowed scalogram difference (see Bolos et al. (2017) <doi:10.1016/j.amc.2017.05.046>), scale index and windowed scale index (Benitez et al. (2010) <doi:10.1016/j.camwa.2010.05.010>).
	"""
	
	cran = "wavScalogram" 

	version("1.1.3", md5="7643a7a9d94261c6cfc3e4788f913780")
	version("1.1.2", md5="2586238bbab4b023d269d2dc0496e274")

	depends_on("r-abind", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
