# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsignal(RPackage):
	"""Signal Processing

	R implementation of the 'Octave' package 'signal', containing
    a variety of signal processing tools, such as signal generation and
    measurement, correlation and convolution, filtering, filter design,
    filter analysis and conversion, power spectrum analysis, system
    identification, decimation and sample rate change, and windowing.
	"""
	
	homepage = "https://github.com/gjmvanboxtel/gsignal"
	cran = "gsignal" 

	version("0.3-5", md5="75ee9ce9ea4efaba70efe3966d6b950d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
