# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPreferably(RPackage):
	"""A 'pkgdown' Template

	This is an accessible template for 'pkgdown'. It uses two
    bootstrap themes, Flatly and Darkly and utilizes the
    'prefers-color-scheme' CSS variable to automatically serve either of
    the two based on user’s operating system setting, or allowing them to
    manually toggle between them.
	"""
	
	homepage = "https://preferably.amirmasoudabdol.name"
	cran = "preferably" 

	version("0.4.1", md5="11aabc1663fa9ee2d07ce61d3d1dffa6")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-pkgdown", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
