# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDecompdl(RPackage):
	"""Decomposition Based Deep Learning Models for Time Series
Forecasting

	Hybrid model is the most promising forecasting method by combining decomposition and deep learning techniques to improve the accuracy of time series forecasting. Each decomposition technique decomposes a time series into a set of intrinsic mode functions (IMFs), and the obtained IMFs are modelled and forecasted separately using the deep learning models. Finally, the forecasts of all IMFs are combined to provide an ensemble output for the time series. The prediction ability of the developed models are calculated using international monthly price series of maize in terms of evaluation criteria like root mean squared error, mean absolute percentage error and, mean absolute error. For method details see Choudhary, K. et al. (2023). <https://ssca.org.in/media/14_SA44052022_R3_SA_21032023_Girish_Jha_FINAL_Finally.pdf>.
	"""
	
	cran = "decompDL" 

	version("0.1.0", md5="54058239c949c9ca46f3f9ee87b8dfe8")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-keras", type=("build", "run"))
	depends_on("r-tensorflow", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-tsutils", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlibeemd", type=("build", "run"))
	depends_on("r-tsdeeplearning", type=("build", "run"))
	depends_on("r-vmdecomp", type=("build", "run"))
