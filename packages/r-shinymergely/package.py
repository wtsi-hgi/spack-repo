# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinymergely(RPackage):
	"""Compare and Merge Two Files with a 'Shiny' App

	A 'Shiny' app allowing to compare and merge two files, with syntax highlighting for several coding languages.
	"""
	
	homepage = "https://github.com/stla/shinyMergely"
	cran = "shinyMergely" 

	version("0.2.0", md5="1cc507943440437e676ba1dea3235442")

	depends_on("r-shiny", type=("build", "run"))
