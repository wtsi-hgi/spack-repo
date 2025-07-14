# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRain(RPackage):
	"""Rhythmicity Analysis Incorporating Non-parametric Methods

	This package uses non-parametric methods to detect rhythms in time series. It deals with outliers, missing values and is optimized for time series comprising 10-100 measurements. As it does not assume expect any distinct waveform it is optimal or detecting oscillating behavior (e.g. circadian or cell cycle) in e.g. genome- or proteome-wide biological measurements such as: micro arrays, proteome mass spectrometry, or metabolome measurements.
	"""
	
	bioc = "rain" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/rain_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/rain/rain_1.36.0.tar.gz"]

	version("1.42.0", tag="RELEASE_3_21")
	version("1.36.0", sha256="be4abaf00359a79fcafd2d18ac5b932c7ac12c4fb32edb2e0ed536e9e144c931")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-gmp", type=("build", "run"))
	depends_on("r-multtest", type=("build", "run"))
