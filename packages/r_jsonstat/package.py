# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJsonstat(RPackage):
	"""Interface to 'JSON-stat'

	Interface to 'JSON-stat' <https://json-stat.org/>,
  a simple lightweight 'JSON' format for data dissemination.
	"""
	
	homepage = "https://github.com/zedoul/jsonstat"
	cran = "jsonstat" 

	version("0.0.2", md5="3095b107db1482680c999c6b36204962")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
