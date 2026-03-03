# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRstatscn(RPackage):
	"""R Interface for China National Data

	R interface for china national data <http://data.stats.gov.cn/>, 
    some convenient functions for accessing the national data are provided.
	"""
	
	homepage = "http://www.bagualu.net/"
	cran = "rstatscn" 

	version("1.1.3", md5="dc7e87167666a90b104e90953da29b7f")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-httr@1:", type=("build", "run"))
	depends_on("r-jsonlite@0.9.19:", type=("build", "run"))
