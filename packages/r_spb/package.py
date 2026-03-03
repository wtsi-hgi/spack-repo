# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpb(RPackage):
	"""Simple Progress Bars for Procedural Coding

	Provides a simple progress bar to use for basic and advanced users that suits all those who prefer procedural programming. It is especially useful for integration into markdown files thanks to the progress bar's customisable appearance.
	"""
	
	cran = "SPB" 

	version("1.0", md5="e6e253c187be5d864d787588e551c239")

	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
