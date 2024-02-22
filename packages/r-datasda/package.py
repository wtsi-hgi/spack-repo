# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatasda(RPackage):
	"""Data Sets for Symbolic Data Analysis

	Collects a diverse range of symbolic data and offers a comprehensive set of functions that facilitate the conversion of traditional data into the symbolic data format.
	"""
	
	cran = "dataSDA" 

	version("0.1.0", md5="29fa3a518c26ac9b2e2b2b57f4ca457b")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
