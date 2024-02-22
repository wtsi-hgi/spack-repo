# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpanel(RPackage):
	"""Simple Interactive Controls for R using the 'tcltk' Package

	A set of functions to build simple 
        GUI controls for R functions.  These are built on the 'tcltk' package. 
        Uses could include changing a parameter on a graph by animating it 
        with a slider or a "doublebutton", up to more sophisticated control 
        panels.
        Some functions for specific graphical tasks, referred to as 'cartoons',
        are provided.
	"""
	
	cran = "rpanel" 

	version("1.1-5.2", md5="1e592a36b57c13d99544b0c1439377a0")

	depends_on("r@3:", type=("build", "run"))
