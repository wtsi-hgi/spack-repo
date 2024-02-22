# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSoyurt(RPackage):
	"""USDA Northern Region Uniform Soybean Tests Dataset

	Data sets used by 'Krause et al. (2022)'  <doi:10.1101/2022.04.11.487885>. It comprises phenotypic records obtained from the USDA Northern Region Uniform Soybean Tests from 1989 to 2019 for maturity groups II and III. In addition, soil and weather variables are provided for the 591 observed environments (combination of locations and years).
	"""
	
	homepage = "https://github.com/mdkrause/soyurt"
	cran = "SoyURT" 

	version("1.0.0", md5="a7046d34d17acd1344bc6b1b7f2281b3")

	depends_on("r@3.5:", type=("build", "run"))
