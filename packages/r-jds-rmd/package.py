# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJdsRmd(RPackage):
	"""R Markdown Templates for Journal of Data Science

	
    Customized R Markdown templates for authoring articles
    for Journal of Data Science.
	"""
	
	homepage = "https://github.com/wenjie2wang/jds.rmd"
	cran = "jds.rmd" 

	version("0.3.3", md5="4ff18d26bc36e45d80c039df384306a7")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-bookdown", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
