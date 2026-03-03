# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCzso(RPackage):
	"""Use Open Data from the Czech Statistical Office in R

	Get programmatic access to the open data provided by the
    Czech Statistical Office (CZSO, <https://czso.cz>).
	"""
	
	homepage = "https://github.com/petrbouchal/czso"
	cran = "czso" 

	version("0.3.10", md5="6874607df017f7ce05a8e6e70d9344d6")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-curl@4.3:", type=("build", "run"))
	depends_on("r-dplyr@0.8.3:", type=("build", "run"))
	depends_on("r-httr@1.4.1:", type=("build", "run"))
	depends_on("r-jsonlite@1.6:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-readr@1.3.1:", type=("build", "run"))
	depends_on("r-rlang@0.4.4:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-tibble@2.1.3:", type=("build", "run"))
