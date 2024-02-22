# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGcxgclab(RPackage):
	"""GCxGC Preprocessing and Analysis

	Provides complete detailed preprocessing of two-dimensional gas chromatogram (GCxGC) samples. Baseline correction, smoothing, peak detection, and peak alignment. Also provided are some analysis functions, such as finding extracted ion chromatograms, finding mass spectral data, targeted analysis, and nontargeted analysis with either the 'National Institute of Standards and Technology Mass Spectral Library' or with the mass data. There are also several visualization methods provided for each step of the preprocessing and analysis.
	"""
	
	cran = "gcxgclab" 

	version("1.0.1", md5="a0bd7b92e7c6fffff18b1a451d9876f9")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-ncdf4@1.19:", type=("build", "run"))
	depends_on("r-dplyr@1.0.8:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-ptw@1.9.16:", type=("build", "run"))
	depends_on("r-nilde@1.1.6:", type=("build", "run"))
	depends_on("r-zoo@1.8.11:", type=("build", "run"))
	depends_on("r-nls-multstart@1.3:", type=("build", "run"))
	depends_on("r-rdpack@2.4:", type=("build", "run"))
