# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinytester(RPackage):
	"""Functions to Minimize Bonehead Moves While Working with 'shiny'

	It's my experience that working with 'shiny' is intuitive once you're
    into it, but can be quite daunting at first. Several common mistakes are fairly
    predictable, and therefore we can control for these. The functions in this
    package help match up the assets listed in the UI and the SERVER files, and
    Visualize the ad hoc structure of the 'shiny' App.
	"""
	
	cran = "ShinyTester" 

	version("0.1.0", md5="1c13a1c1fe3af0984fee0d59b330482d")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
