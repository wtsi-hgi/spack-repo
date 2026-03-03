# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMidas(RPackage):
	"""Turn HTML 'Shiny'

	Contains functions for converting existing HTML/JavaScript
   source into equivalent 'shiny' functions. Bootstraps the process of making
   new 'shiny' functions by allowing us to turn HTML snippets directly into 
   R functions.
	"""
	
	cran = "midas" 

	version("1.0.1", md5="9495f4e2ca535007e6d817e718616559")

	depends_on("r-shiny@1.0.3:", type=("build", "run"))
	depends_on("r-xml2@1.1.1:", type=("build", "run"))
