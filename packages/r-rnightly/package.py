# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnightly(RPackage):
	"""A Wrapper of the 'JavaScript' Library 'Nightly'

	Allows the user to implement a dark/light toggle mode in 'shiny' using the 'Nightly' 'JavaScript' library. 
    The default mode is dark/light however the user can also specify other colours.
	"""
	
	homepage = "https://github.com/feddelegrand7/Rnightly"
	cran = "Rnightly" 

	version("0.1.0", md5="a82d98d778dd19a852f569dcd2c961b6")

	depends_on("r-glue", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
