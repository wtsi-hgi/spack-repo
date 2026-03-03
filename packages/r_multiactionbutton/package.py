# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultiactionbutton(RPackage):
	"""Multi Action Button for 'Shiny' Applications

	Provides a multi action button for usage in 'shiny'
    applications.
	"""
	
	homepage = "https://github.com/stla/multiActionButton"
	cran = "multiActionButton" 

	version("1.0.0", md5="51d4f874ba73eacb366ab1c0332afb72")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
