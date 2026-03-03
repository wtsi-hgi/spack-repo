# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRealtimeloads(RPackage):
	"""Analyte Flux and Load from Estimates of Concentration and
Discharge

	Flux (mass per unit time) and Load (mass) are computed from timeseries estimates of analyte concentration and discharge. Concentration timeseries are computed from regression between surrogate and user-provided analyte. Uncertainty in calculations is estimated using bootstrap resampling. Code for the processing of acoustic backscatter from horizontally profiling acoustic Doppler current profilers is provided. All methods detailed in Livsey et al (2020) <doi:10.1007/s12237-020-00734-z>, Livsey et al (2023) <doi:10.1029/2022WR033982>, and references therein.
	"""
	
	cran = "realTimeloads" 

	version("1.0.0", md5="e27736d237caa80f7b086e6a6c2a26db")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-imputets", type=("build", "run"))
	depends_on("r-mice", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-tideharmonics", type=("build", "run"))
