# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMwshiny(RPackage):
	"""'Shiny' for Multiple Windows

	A simple function, mwsApp(), that runs a 'shiny' app spanning multiple,
  connected windows. This uses all standard 'shiny' conventions, and depends only on
  the 'shiny' package.
	"""
	
	cran = "mwshiny" 

	version("2.1.0", md5="8d76100328f8f2963242123b94c76118")

	depends_on("r-shiny@1.2:", type=("build", "run"))
	depends_on("r-htmltools@0.3.6:", type=("build", "run"))
