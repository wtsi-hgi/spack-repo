# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrecintcon(RPackage):
	"""Precipitation Intensity, Concentration and Anomaly Analysis

	It contains functions to analyze the precipitation
    intensity, concentration and anomaly.
	"""
	
	homepage = "https://github.com/lucasvenez/precintcon"
	cran = "precintcon" 

	version("2.3.0", md5="9b7096337eb8715bc4b2f84bae80543b")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
