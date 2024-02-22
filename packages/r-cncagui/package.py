# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCncagui(RPackage):
	"""Canonical Non-Symmetrical Correspondence Analysis in R

	A GUI with which users can construct and interact
        with Canonical Correspondence Analysis and Canonical Non-Symmetrical Correspondence Analysis and provides inferential results by using Bootstrap Methods.
	"""
	
	cran = "cncaGUI" 

	version("1.1", md5="acdafa3258dee9c367246742d892e3d9")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-tkrplot", type=("build", "run"))
	depends_on("r-tcltk2", type=("build", "run"))
	depends_on("r-shapes", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
