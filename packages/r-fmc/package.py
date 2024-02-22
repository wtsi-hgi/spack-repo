# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFmc(RPackage):
	"""Factorial Experiments with Minimum Level Changes

	Generate cost effective minimally changed run sequences 
              for symmetrical as well as asymmetrical factorial 
              designs.
	"""
	
	cran = "FMC" 

	version("1.0.1", md5="0e00aece95cb785acbae603bbc2a41d9")

	depends_on("r-minimalrsd", type=("build", "run"))
