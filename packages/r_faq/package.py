# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFaq(RPackage):
	"""Create FAQ Page

	Create Frequently Asked Questions page for Shiny application.
	"""
	
	cran = "faq" 

	version("0.1.1", md5="6e6c3435bc7a4099d55775360ff6f01d")

	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
