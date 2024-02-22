# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCnum(RPackage):
	"""Chinese Numerals Processing

	Chinese numerals processing in R, such as conversion between 
    Chinese numerals and Arabic numerals as well as detection and extraction of
    Chinese numerals in character objects and string. This package supports 
    the casual scale naming system and the respective SI prefix systems used 
    in mainland China and Taiwan: 
    "China Statutory Measurement Units"
    State Administration for Market Regulation (2019) <http://gkml.samr.gov.cn/nsjg/jls/201902/t20190225_291134.html>
    "Names, Definitions and Symbols of the Legal Units of Measurement and the Decimal Multiples and Submultiples" 
    Ministry of Economic Affairs (2019) <https://gazette.nat.gov.tw/egFront/detail.do?metaid=108965>.
	"""
	
	homepage = "https://github.com/elgarteo/cnum/"
	cran = "cnum" 

	version("0.1.3", md5="3cb5ab3fdaf4277d1ebfbe147e8990e1")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
