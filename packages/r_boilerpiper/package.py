# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBoilerpiper(RPackage):
	"""Interface to the Boilerpipe Java Library

	Generic Extraction of main text content from HTML files; removal
    of ads, sidebars and headers using the boilerpipe 
    <https://github.com/kohlschutter/boilerpipe> Java library. The
    extraction heuristics from boilerpipe show a robust performance for a wide
    range of web site templates.
	"""
	
	homepage = "https://github.com/mannau/boilerpipeR"
	cran = "boilerpipeR" 

	version("1.3.2", md5="88decc37d99075dd144c05049bf9650b")

	depends_on("r-rjava", type=("build", "run"))
