# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROttrpal(RPackage):
	"""Companion Tools for Open-Source Tools for Training Resources
(OTTR)

	Tools for converting Open-Source Tools for Training Resources
    (OTTR) courses into Leanpub or Coursera courses. 'ottrpal' is for use
    with the OTTR Template repository to create courses.
	"""
	
	homepage = "https://github.com/jhudsl/ottrpal"
	cran = "ottrpal" 

	version("1.2.1", md5="401d1f7d1711b9cec09db6e07de6b36c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bookdown", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-knitr@1.33:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rmarkdown@2.10:", type=("build", "run"))
	depends_on("r-rprojroot", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
