# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAos(RPackage):
	"""Animate on Scroll Library for 'shiny'

	Trigger animation effects on scroll on any HTML element 
    of 'shiny' and 'rmarkdown', such as any text or plot, thanks to 
    the 'AOS' Animate On Scroll jQuery library.
	"""
	
	homepage = "https://felixluginbuhl.com/aos"
	cran = "aos" 

	version("0.1.0", md5="b73273a003f0de212d4a66e1119b39a5")

	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
