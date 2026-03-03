# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNpphen(RPackage):
	"""Vegetation Phenological Cycle and Anomaly Detection using Remote
Sensing Data

	Calculates phenological cycle and anomalies using a non-parametric
    approach applied to time series of vegetation indices derived from remote sensing data 
    or field measurements. The package implements basic and high-level functions for 
    manipulating vector data (numerical series) and raster data (satellite derived products).
    Processing of very large raster files is supported. For more information, please check 
    the following paper:
    Chávez et al. (2023) <doi:10.3390/rs15010073>.
	"""
	
	homepage = "https://github.com/labGRS/npphen"
	cran = "npphen" 

	version("2.0.0", md5="5616062b41d2a2c0f983ecc1d2e46645")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-terra@1.5.17:", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
