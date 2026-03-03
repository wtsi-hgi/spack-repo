# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArabic2kansuji(RPackage):
	"""Convert Arabic Numerals to Kansuji

	Simple functions to convert given Arabic numerals to Kansuji  
    numerical figures that represent numbers written in Chinese characters.
	"""
	
	homepage = "https://github.com/indenkun/arabic2kansuji"
	cran = "arabic2kansuji" 

	version("0.1.3", md5="263ab9fe49b65177f36326026aa4c220")

	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
