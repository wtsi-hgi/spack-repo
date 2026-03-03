# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAwsWrfsmn(RPackage):
	"""Data Processing of SMN Hi-Res Weather Forecast from 'AWS'

	Exploration of Weather Research & Forecasting ('WRF') Model data
    of Servicio Meteorologico Nacional (SMN) from Amazon Web Services
    (<https://registry.opendata.aws/smn-ar-wrf-dataset/>) cloud. The package
    provides the possibility of data downloading, processing and correction
    methods. It also has map management and series exploration of available
    meteorological variables of 'WRF' forecast.
	"""
	
	cran = "aws.wrfsmn" 

	version("0.0.3", md5="877db0a8eca3aa383836639da1b605e0")
	version("0.0.1", md5="cd093480c0f137b1dccd4c547087fc74")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-aws-s3@0.3.21:", type=("build", "run"))
	depends_on("r-lubridate@1.9.3:", type=("build", "run"))
	depends_on("r-terra@1.7.65:", type=("build", "run"))
	depends_on("r-dplyr@1.1.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.4.4:", type=("build", "run"))
	depends_on("r-hydrogof@0.5.4:", type=("build", "run"))
	depends_on("r-magrittr@2.0.3:", type=("build", "run"))
