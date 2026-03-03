# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRticles(RPackage):
	"""Article Formats for R Markdown

	A suite of custom R Markdown formats and templates for
    authoring journal articles and conference submissions.
	"""
	
	homepage = "https://github.com/rstudio/rticles"
	cran = "rticles" 

	version("0.26", md5="f8c3f30decffe317001d7fa61d0662f8")

	depends_on("r-knitr@1.30:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rmarkdown@2.14:", type=("build", "run"))
	depends_on("r-tinytex@0.30:", type=("build", "run"))
	depends_on("r-xfun", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
