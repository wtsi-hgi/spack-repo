# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAndurinha(RPackage):
	"""Make Spectroscopic Data Processing Easier

	The goal of 'andurinha' is provide a fast and friendly way to 
    process spectroscopic data. It is intended for processing several spectra of 
    samples with similar composition (tens to hundreds of spectra). It compiles 
    spectroscopy data files, produces standardized and second derivative spectra, 
    finds peaks and allows to select the most significant ones based on the second 
    derivative/absorbance sum spectrum. It also provides functions for graphic 
    evaluation of the outputs.
	"""
	
	homepage = "https://github.com/noemiallefs/andurinha"
	cran = "andurinha" 

	version("0.0.2", md5="76a46c1ce718c92492da1f39e713b1ec")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
