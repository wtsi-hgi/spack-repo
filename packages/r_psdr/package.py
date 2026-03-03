# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsdr(RPackage):
	"""Use Time Series to Generate and Compare Power Spectral Density

	Functions that allow you to generate and compare power spectral density (PSD) 
	plots given time series data. Fast Fourier Transform (FFT) is used to take a time series 
	data, analyze the oscillations, and then output the frequencies of these oscillations 
	in the time series in the form of a PSD plot.Thus given a time series, the dominant 
	frequencies in the time series can be identified. Additional functions in this package 
	allow the dominant frequencies of multiple groups of time series to be compared with each other. 
	To see example usage with the main functions of this package, please visit
	this site: <https://yhhc2.github.io/psdr/articles/Introduction.html>. 
	The mathematical operations used to generate the PSDs are described in these sites:
	<https://www.mathworks.com/help/matlab/ref/fft.html>.
	<https://www.mathworks.com/help/signal/ug/power-spectral-density-estimates-using-fft.html>.
	"""
	
	cran = "psdr" 

	version("1.0.1", md5="a415997bbabdb24f627ea0af10082deb")

	depends_on("r-devtools@2.4.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.2:", type=("build", "run"))
	depends_on("r-qpdf@1.1:", type=("build", "run"))
