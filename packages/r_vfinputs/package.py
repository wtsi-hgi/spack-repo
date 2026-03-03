# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVfinputs(RPackage):
	"""Visual Filter Inputs for Shiny

	A set of visual input controls for Shiny apps to facilitate filtering across multiple outputs.
	"""
	
	homepage = "https://github.com/rhenkin/vfinputs"
	cran = "vfinputs" 

	version("0.1.0", md5="219ddcebc1d856ff829178652636b72e")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
