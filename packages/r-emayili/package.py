# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmayili(RPackage):
	"""Send Email Messages

	A light, simple tool for sending emails with minimal dependencies.
	"""
	
	homepage = "https://datawookie.github.io/emayili/"
	cran = "emayili" 

	version("0.7.18", md5="08d5a2078d6bfd0cef4b84a0e31da72d")

	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-commonmark", type=("build", "run"))
	depends_on("r-curl@4:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-logger", type=("build", "run"))
	depends_on("r-magrittr@2.0.1:", type=("build", "run"))
	depends_on("r-mime", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-urltools", type=("build", "run"))
	depends_on("r-xfun", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("pandoc", type=("build", "link", "run"))
