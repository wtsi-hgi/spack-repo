# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeflatebr(RPackage):
	"""Deflate Nominal Brazilian Reais

	Simple functions to deflate nominal Brazilian Reais using several popular price indexes downloaded from the Brazilian Institute for Applied Economic Research.
	"""
	
	homepage = "https://github.com/meirelesff/deflatebr/"
	cran = "deflateBR" 

	version("1.1.2", md5="1effac635a5cbcf52f7dc55a9eed4f8a")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-dplyr@0.5:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
