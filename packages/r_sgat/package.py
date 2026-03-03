# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSgat(RPackage):
	"""Extract Information from Google's "Popular Times"

	Once you've identified a real life place, such as a shop, a restaurant, a bar, etc. use this package to simulate a Google search and retrieve its "Popular Times" and geographic location information and save them in Comma-Separated Values files. This package also downloads a list of restaurants and bars of Ushuaia city, Argentina.
	"""
	
	homepage = "https://github.com/matiaspoullain/sgat"
	cran = "sgat" 

	version("0.9", md5="02221229562eec7df0de686c29eb3d6a")

	depends_on("r-rselenium", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-qdapregex", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
