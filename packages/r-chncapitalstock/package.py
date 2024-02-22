# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChncapitalstock(RPackage):
	"""Compute Chinese Capital Stocks

	Compute Chinese capital stocks in provinces level, based on Zhang (2008) <DOI:10.1080/14765280802028302>. 
	"""
	
	homepage = "https://github.com/common2016/CapitalStock"
	cran = "CHNCapitalStock" 

	version("0.1.1", md5="b4cea2cec2447f1aa0a6864bad652734")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
