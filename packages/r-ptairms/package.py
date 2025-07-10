# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPtairms(RPackage):
	"""Pre-processing PTR-TOF-MS Data

	This package implements a suite of methods to preprocess data from PTR-TOF-MS instruments (HDF5 format) and generates the 'sample by features' table of peak intensities in addition to the sample and feature metadata (as a singl<e ExpressionSet object for subsequent statistical analysis). This package also permit usefull tools for cohorts management as analyzing data progressively, visualization tools and quality control. The steps include calibration, expiration detection, peak detection and quantification, feature alignment, missing value imputation and feature annotation. Applications to exhaled air and cell culture in headspace are described in the vignettes and examples. This package was used for data analysis of Gassin Delyle study on adults undergoing invasive mechanical ventilation in the intensive care unit due to severe COVID-19 or non-COVID-19 acute respiratory distress syndrome (ARDS), and permit to identfy four potentiel biomarquers of the infection.
	"""
	
	bioc = "ptairMS" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ptairMS_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ptairMS/ptairMS_1.10.0.tar.gz"]

	version("1.10.0", sha256="1fa231c1c9aa28ac336710e12eed0611a23b0a1ed09e98e38246b61d525f5662")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-bit64", type=("build", "run"))
	depends_on("r-chron", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-envipat", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-msnbase", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyscreenshot", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
