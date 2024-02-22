# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REemdlstm(RPackage):
	"""EEMD Based LSTM Model for Time Series Forecasting

	Forecasting univariate time series with ensemble empirical mode decomposition (EEMD) with long short-term memory (LSTM). For method details see Jaiswal, R. et al. (2022). <doi:10.1007/s00521-021-06621-3>. 
	"""
	
	cran = "EEMDlstm" 

	version("0.1.0", md5="40dbccfdd1909fd9e88a9278b19f4e32")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-keras", type=("build", "run"))
	depends_on("r-tensorflow", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-tsutils", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlibeemd", type=("build", "run"))
	depends_on("r-tsdeeplearning", type=("build", "run"))
