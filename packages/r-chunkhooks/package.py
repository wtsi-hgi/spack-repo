# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChunkhooks(RPackage):
	"""Chunk Hooks for 'R Markdown'

	
    Set chunk hooks for 'R Markdown' documents <https://rmarkdown.rstudio.com/>,
    and improve user experience.
    For example, change units of figure sizes, benchmark chunks, and number
    lines on code blocks.
	"""
	
	homepage = "https://chunkhooks.atusy.net"
	cran = "chunkhooks" 

	version("0.0.1", md5="01c36d2ac00fe260ef0f882c83316c89")

	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-measurements", type=("build", "run"))
	depends_on("r-prettyunits", type=("build", "run"))
