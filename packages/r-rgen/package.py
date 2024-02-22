# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgen(RPackage):
	"""Random Sampling Distribution C++ Routines for Armadillo

	Provides popular sampling distributions C++ routines based in 
    armadillo through a header file approach.
	"""
	
	cran = "rgen" 

	version("0.0.1", md5="67437443da56cb283d90b95fb413e843")

	depends_on("r@3.3:", type=("build", "run"))
