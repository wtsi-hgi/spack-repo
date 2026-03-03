# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpeaq(RPackage):
	"""Tools for Nuclear Magnetic Resonance (NMR) Spectra Alignment,
Peak Based Processing, Quantitative Analysis and Visualizations

	Makes Nuclear Magnetic Resonance spectroscopy (NMR spectroscopy) data analysis as easy as possible by only requiring a small set of functions to perform an entire analysis. 'speaq' offers the possibility of raw spectra alignment and quantitation but also an analysis based on features whereby the spectra are converted to peaks which are then grouped and turned into features. These features can be processed with any number of statistical tools either included in 'speaq' or available elsewhere on CRAN. More details can be found in Vu et al. (2011) <doi:10.1186/1471-2105-12-405> and Beirnaert et al. (2018) <doi:10.1371/journal.pcbi.1006018>. 
	"""
	
	cran = "speaq" 

	version("2.7.0", md5="d9985ffc91cfd66dbe748a13f91cec40")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-massspecwavelet", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-missforest", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
