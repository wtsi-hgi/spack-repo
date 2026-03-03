# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMemor(RPackage):
	"""A 'rmarkdown' Template that Can be Highly Customized

	A 'rmarkdown' template that supports company logo, contact info, 
    watermarks and more. Currently restricted to 'Latex'/'Markdown'; a similar 
    'HTML' theme will be added in the future. 
	"""
	
	homepage = "https://github.com/hebrewseniorlife/memor"
	cran = "memor" 

	version("0.2.3", md5="8c8f22b6610f847948177abd2eb5717b")

	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
