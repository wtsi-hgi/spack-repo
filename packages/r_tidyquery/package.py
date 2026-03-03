# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidyquery(RPackage):
	"""Query 'R' Data Frames with 'SQL'

	Use 'SQL' 'SELECT' statements to query 'R' data
    frames.
	"""
	
	homepage = "https://github.com/ianmcook/tidyquery"
	cran = "tidyquery" 

	version("0.2.4", md5="10ec1fe77a96092b5955b12364d060fc")

	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-lubridate@1.6:", type=("build", "run"))
	depends_on("r-queryparser@0.3.2:", type=("build", "run"))
	depends_on("r-rlang@0.4.9:", type=("build", "run"))
	depends_on("r-stringr@1:", type=("build", "run"))
