# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPergola(RPackage):
	"""Toolbox for Polyploid Genetic Data

	Provides tools for linkage mapping in polyploids.
    It implements the method PERGOLA, which is a fast, deterministic method to
    calculate the order of markers in a linkage group.
	"""
	
	homepage = "http://github.com/grafab/pergola"
	cran = "pergola" 

	version("1.0", md5="56c786e5e9246d5ae750e2a6165876b1")

	depends_on("r-seriation", type=("build", "run"))
