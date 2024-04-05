# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXaringan(RPackage):
	"""Presentation Ninja

	Create HTML5 slides with R Markdown and the JavaScript library
    'remark.js' (<https://remarkjs.com>).
	"""
	
	homepage = "https://github.com/yihui/xaringan"
	cran = "xaringan" 

	version("0.30", md5="49ff7b601b05c68bf6165ade30a4a6f7")
	version("0.29", md5="cf4df3745a82f912b6dbbb094d4716e5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-knitr@1.30:", type=("build", "run"))
	depends_on("r-servr@0.30:", type=("build", "run"))
	depends_on("r-xfun@0.18:", type=("build", "run"))
	depends_on("r-rmarkdown@2.8:", type=("build", "run"))
