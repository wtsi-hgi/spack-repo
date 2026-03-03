# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsf(RPackage):
	"""Forecasting of Univariate Time Series Using the Pattern
Sequence-Based Forecasting (PSF) Algorithm

	Pattern Sequence Based Forecasting (PSF) takes univariate
    time series data as input and assist to forecast its future values.
    This algorithm forecasts the behavior of time series
    based on similarity of pattern sequences. Initially, clustering is done with the
    labeling of samples from database. The labels associated with samples are then
    used for forecasting the future behaviour of time series data. The further
    technical details and references regarding PSF are discussed in Vignette.
	"""
	
	homepage = "https://www.neerajbokde.in/viggnette/2021-10-13-PSF/"
	cran = "PSF" 

	version("0.5", md5="596320058a4dda846176493b4028f9f8")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
