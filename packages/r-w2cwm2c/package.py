# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RW2cwm2c(RPackage):
	"""A Graphical Tool for Wavelet (Cross) Correlation and Wavelet
Multiple (Cross) Correlation Analysis

	Set of functions that improves the graphical presentations of the functions: wave.correlation and spin.correlation (waveslim package, Whitcher 2012) and the wave.multiple.correlation and wave.multiple.cross.correlation (wavemulcor package, Fernandez-Macho 2012b). The plot outputs (heatmaps) can be displayed in the screen or can be saved as PNG or JPG images or as PDF or EPS formats. The W2CWM2C package also helps to handle the (input data) multivariate time series easily as a list of N elements (times series) and provides a multivariate data set (dataexample) to exemplify its use. A description of the package was published in a scientific paper: Polanco-Martinez and Fernandez-Macho (2014), <doi:10.1109/MCSE.2014.96>. 
	"""
	
	homepage = "https://github.com/jomopo/W2CWM2C"
	cran = "W2CWM2C" 

	version("2.2", md5="1f34854d589dcb56ed599664a8a74328")

	depends_on("r@2.14.1:", type=("build", "run"))
	depends_on("r-waveslim", type=("build", "run"))
	depends_on("r-wavemulcor", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
