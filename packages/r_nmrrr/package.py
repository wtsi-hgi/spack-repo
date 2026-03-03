# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNmrrr(RPackage):
	"""Binning and Visualizing NMR Spectra in Environmental Samples

	A reproducible workflow for binning and visualizing NMR (nuclear magnetic resonance) spectra from environmental samples. The 'nmrrr' package is intended for post-processing of NMR data, including importing, merging and, cleaning data from multiple files, visualizing NMR spectra, performing binning/integrations for compound classes, and relative abundance calculations. 
    This package can be easily inserted into existing analysis workflows by users to help with analyzing and interpreting NMR data. 
	"""
	
	homepage = "https://github.com/kaizadp/nmrrr"
	cran = "nmrrr" 

	version("1.0.0", md5="d6ef3ae28fb063ad3933b21b99e2d4c0")

	depends_on("r@3.50:", type=("build", "run"))
	depends_on("r-desctools", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
