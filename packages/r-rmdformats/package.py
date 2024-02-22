# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmdformats(RPackage):
	"""HTML Output Formats and Templates for 'rmarkdown' Documents

	HTML formats and templates for 'rmarkdown' documents, with some extra
    features such as automatic table of contents, lightboxed figures, dynamic
    crosstab helper.
	"""
	
	homepage = "https://github.com/juba/rmdformats"
	cran = "rmdformats" 

	version("1.0.4", md5="fc2e2973a14068c24888cf4250e7561f")

	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-bookdown", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
