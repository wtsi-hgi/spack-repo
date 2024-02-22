# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKeys(RPackage):
	"""Keyboard Shortcuts for 'shiny'

	Assign and listen to keyboard shortcuts in 'shiny' using the 
  'Mousetrap' Javascript library.
	"""
	
	homepage = "https://github.com/r4fun/keys"
	cran = "keys" 

	version("0.1.1", md5="9be14f262ba19eff3fa194881c5e8fb1")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
