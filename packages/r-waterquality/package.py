# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWaterquality(RPackage):
	"""Satellite Derived Water Quality Detection Algorithms

	The main purpose of waterquality is to quickly and easily convert
    satellite-based reflectance imagery into one or many well-known water quality
    algorithms designed for the detection of harmful algal blooms or the following
    pigment proxies: chlorophyll-a, blue-green algae (phycocyanin), and turbidity.
    Johansen et al. (2019) <doi:10.21079/11681/35053>. 
	"""
	
	homepage = "https://github.com/RAJohansen/waterquality"
	cran = "waterquality" 

	version("1.0.0", md5="67015c1ccf726d97aa9520ba5bfd1cd3")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
