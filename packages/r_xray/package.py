# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXray(RPackage):
	"""X Ray Vision on your Datasets

	Tools to analyze datasets previous to any statistical modeling.
    Has various functions designed to find inconsistencies and understanding the distribution of the data.
	"""
	
	homepage = "https://github.com/sicarul/xray/"
	cran = "xray" 

	version("0.2", md5="6d05aaa464df608ba62a684342900760")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
