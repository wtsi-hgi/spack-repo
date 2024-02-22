# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSummariser(RPackage):
	"""Easy Calculation and Visualisation of Confidence Intervals

	Functions to speed up the exploratory analysis of simple
    datasets using 'dplyr'. Functions are provided to do the 
    common tasks of calculating confidence intervals.
	"""
	
	homepage = "https://github.com/condwanaland/summariser"
	cran = "summariser" 

	version("2.3.0", md5="cda55df52f11782186656c2ffb076f85")

	depends_on("r-dplyr", type=("build", "run"))
