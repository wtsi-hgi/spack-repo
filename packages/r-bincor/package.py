# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBincor(RPackage):
	"""Estimate the Correlation Between Two Irregular Time Series

	Estimate the correlation between two irregular time series that are not necessarily sampled on identical time points. This program is also applicable to the situation of two evenly spaced time series that are not on the same time grid. 'BINCOR' is based on a novel estimation approach proposed by Mudelsee (2010, 2014) to estimate the correlation between two climate time series with different timescales. The idea is that autocorrelation (AR1 process) allows to correlate values obtained on different time points. 'BINCOR' contains four functions: bin_cor() (the main function to build the binned time series), plot_ts() (to plot and compare the irregular and binned time series, cor_ts() (to estimate the correlation between the binned time series) and ccf_ts() (to estimate the cross-correlation between the binned time series).
	"""
	
	cran = "BINCOR" 

	version("0.2.0", md5="e170504dbfbc93b4ef163ee28efbb8b6")

	depends_on("r-pracma", type=("build", "run"))
