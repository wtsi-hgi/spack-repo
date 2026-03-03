# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyscreenshot(RPackage):
	"""Capture Screenshots of Entire Pages or Parts of Pages in 'Shiny'

	Capture screenshots in 'Shiny' applications. Screenshots can either be
    of the entire viewable page, or a specific section of the page. The captured
    image is automatically downloaded as a PNG image, or it can also be saved on
    the server. Powered by the 'html2canvas' JavaScript library.
	"""
	
	homepage = "https://github.com/daattali/shinyscreenshot"
	cran = "shinyscreenshot" 

	version("0.2.1", md5="8aa346f9bfc743f2837e649732a7592f")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-htmltools@0.3.5:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-shiny@1:", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
