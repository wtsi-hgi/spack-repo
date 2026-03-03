# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDistill(RPackage):
	"""'R Markdown' Format for Scientific and Technical Writing

	Scientific and technical article format for the web.
    'Distill' articles feature attractive, reader-friendly typography,
    flexible layout options for visualizations, and full support for
    footnotes and citations.
	"""
	
	homepage = "https://github.com/rstudio/distill"
	cran = "distill" 

	version("1.6", md5="eb638b9b04227e95dc21b01ae1c00b77")

	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-bookdown@0.8:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-downlit@0.4.1:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-jsonlite@1.3:", type=("build", "run"))
	depends_on("r-knitr@1.15.6:", type=("build", "run"))
	depends_on("r-lubridate@1.7.10:", type=("build", "run"))
	depends_on("r-mime", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-rmarkdown@2.11:", type=("build", "run"))
	depends_on("r-rprojroot", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-whisker", type=("build", "run"))
	depends_on("r-xfun@0.18:", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
