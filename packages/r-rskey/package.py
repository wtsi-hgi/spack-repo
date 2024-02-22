# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRskey(RPackage):
	"""Create Custom 'Rstudio' Keyboard Shortcuts

	Create custom keyboard shortcuts to examine code selected in the 'Rstudio' editor.
             F3 can for example yield 'str(selection)' and F7 open the source
             code of CRAN and base package functions on 'github'.
	"""
	
	cran = "rskey" 

	version("0.4.4", md5="3822c87c70af141c773c59ec1a9559c8")

	depends_on("r-rstudioapi@0.5:", type=("build", "run"))
	depends_on("r-berryfunctions@1.17.21:", type=("build", "run"))
