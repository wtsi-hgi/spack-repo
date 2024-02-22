# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinylogs(RPackage):
	"""Record Everything that Happens in a 'Shiny' Application

	Track and record the use of applications and the user's interactions with 'Shiny' inputs.
  Allows to trace the inputs with which the user interacts, the outputs generated, 
  as well as the errors displayed in the interface.
	"""
	
	homepage = "https://github.com/dreamRs/shinylogs"
	cran = "shinylogs" 

	version("0.2.1", md5="25ffc5c472d557ee69e2d18aa4ae352d")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-shiny@1.1:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-bit64", type=("build", "run"))
	depends_on("r-nanotime", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-anytime", type=("build", "run"))
