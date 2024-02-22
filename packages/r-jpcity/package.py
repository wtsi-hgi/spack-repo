# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJpcity(RPackage):
	"""Read and Convert Japanese Municipality Codes

	Read Japanese city codes (<https://www.e-stat.go.jp/municipalities/cities>) 
    to get city and prefecture names, or convert to city codes at different 
    points in time. In addition, it merges or splits wards of designated cities
    and gets all city codes at a specific point in time.
	"""
	
	homepage = "https://uchidamizuki.github.io/jpcity/"
	cran = "jpcity" 

	version("0.1.1", md5="2e85b00a0215a21ae827dca0c097c0d4")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
