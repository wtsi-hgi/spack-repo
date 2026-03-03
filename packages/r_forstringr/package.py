# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForstringr(RPackage):
	"""String Manipulation Package for Those Familiar with 'Microsoft
Excel'

	The goal of 'forstringr' is to enable complex string
    manipulation in R especially to those more familiar with LEFT(),
    RIGHT(), and MID() functions in Microsoft Excel. The package combines
    the power of 'stringr' with other manipulation packages such as
    'dplyr' and 'tidyr'.
	"""
	
	homepage = "https://github.com/gbganalyst/forstringr"
	cran = "forstringr" 

	version("1.0.0", md5="4eda871db426f796c5ddf98d2d73367b")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
