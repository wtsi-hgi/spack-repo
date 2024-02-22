# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZoomerjoin(RPackage):
	"""Superlatively Fast Fuzzy Joins

	Empowers users to fuzzily-merge data frames with millions or tens of millions of rows in minutes with low memory usage.  The package uses the locality sensitive hashing algorithms developed by Datar, Immorlica, Indyk and Mirrokni (2004) <doi:10.1145/997817.997857>, and Broder (1998) <doi:10.1109/SEQUEN.1997.666900> to avoid having to compare every pair of records in each dataset, resulting in fuzzy-merges that finish in linear time.
	"""
	
	homepage = "https://beniamino.org/zoomerjoin/"
	cran = "zoomerjoin" 

	version("0.1.4", md5="dcc640c2cbce44143a40d3617f1c7aec")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("rust", type=("build", "link", "run"))
