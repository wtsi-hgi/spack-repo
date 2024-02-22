# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnergyr(RPackage):
	"""Data Published by the United States Federal Energy Regulatory
Commission

	Data published by the United States Federal Energy Regulatory Commission including
    electric company financial data, natural gas company financial data, 
    hydropower plant data, liquified natural gas plant data, oil company financial data
    natural gas company financial data, and natural gas storage field data.
	"""
	
	homepage = "https://github.com/paulgovan/energyr"
	cran = "energyr" 

	version("0.1.2", md5="445b59bc6e75ea4e692798008d4b2feb")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rgooglemaps", type=("build", "run"))
