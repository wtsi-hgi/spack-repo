# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSvdialogs(RPackage):
	"""'SciViews' - Standard Dialog Boxes for Windows, MacOS and
Linuxes

	Quickly construct standard dialog boxes for your GUI, including 
  message boxes, input boxes, list, file or directory selection, ... In case R
  cannot display GUI dialog boxes, a simpler command line version of these
  interactive elements is also provided as fallback solution.
	"""
	
	homepage = "https://github.com/SciViews/svDialogs"
	cran = "svDialogs" 

	version("1.1.0", md5="221117c06ec3a116d6c55d6b6c104334")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-svgui@1:", type=("build", "run"))
	depends_on("r-rstudioapi@0.7:", type=("build", "run"))
