# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetathis(RPackage):
	"""HTML Metadata Tags for 'R Markdown' and 'Shiny'

	Create meta tags for 'R Markdown' HTML documents and 'Shiny'
    apps for customized social media cards, for accessibility, and quality
    search engine indexing. 'metathis' currently supports HTML documents
    created with 'rmarkdown', 'shiny', 'xaringan', 'pagedown', 'bookdown',
    and 'flexdashboard'.
	"""
	
	homepage = "https://pkg.garrickadenbuie.com/metathis/"
	cran = "metathis" 

	version("1.1.4", md5="97b21de7871810a703ad27d6425635f1")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
