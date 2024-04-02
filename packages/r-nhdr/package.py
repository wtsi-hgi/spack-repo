# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNhdr(RPackage):
	"""Tools for Working with the National Hydrography Dataset

	Tools for working with the National Hydrography Dataset, with 
    functions for querying, downloading, and networking both the NHD 
    <https://www.usgs.gov/national-hydrography> 
    and NHDPlus <https://www.epa.gov/waterdata/nhdplus-national-hydrography-dataset-plus> datasets. 
	"""
	
	homepage = "https://github.com/jsta/nhdR"
	cran = "nhdR" 

	version("0.6.1", md5="ff9fab228ce036606222826b833d6c26")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
