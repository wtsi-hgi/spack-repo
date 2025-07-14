# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlpsnmr(RPackage):
	"""Automated spectraL Processing System for NMR

	Reads Bruker NMR data directories both zipped and unzipped. It provides automated and efficient signal processing for untargeted NMR metabolomics. It is able to interpolate the samples, detect outliers, exclude regions, normalize, detect peaks, align the spectra, integrate peaks, manage metadata and visualize the spectra. After spectra proccessing, it can apply multivariate analysis on extracted data. Efficient plotting with 1-D data is also available. Basic reading of 1D ACD/Labs exported JDX samples is also available.
	"""
	
	homepage = "https://sipss.github.io/AlpsNMR/"
	bioc = "AlpsNMR"

	version("4.10.0", commit="aa900cfbccb9521c5d520ea5c8f2b7ee386b950d")
	version("4.4.0", commit="30ac1c08a035f1beb4cb53d1ae8cbb11e663f7c5")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-future@1.10:", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-signal@0.7.6:", type=("build", "run"))
	depends_on("r-rlang@0.3.0.1:", type=("build", "run"))
	depends_on("r-scales@1.2:", type=("build", "run"))
	depends_on("r-stringr@1.3.1:", type=("build", "run"))
	depends_on("r-tibble@1.3.4:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-readxl@1.1:", type=("build", "run"))
	depends_on("r-purrr@0.2.5:", type=("build", "run"))
	depends_on("r-glue@1.2:", type=("build", "run"))
	depends_on("r-reshape2@1.4.3:", type=("build", "run"))
	depends_on("r-mixomics@6.22:", type=("build", "run"))
	depends_on("r-matrixstats@0.54:", type=("build", "run"))
	depends_on("r-fs@1.2.6:", type=("build", "run"))
	depends_on("r-rmarkdown@1.10:", type=("build", "run"))
	depends_on("r-speaq@2.4:", type=("build", "run"))
	depends_on("r-htmltools@0.3.6:", type=("build", "run"))
	depends_on("r-pcapp@1.9.73:", type=("build", "run"))
	depends_on("r-ggplot2@3.1:", type=("build", "run"))
	depends_on("r-baseline@1.2.1:", type=("build", "run"))
	depends_on("r-vctrs@0.3:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
