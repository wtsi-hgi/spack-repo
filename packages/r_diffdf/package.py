# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiffdf(RPackage):
	"""Dataframe Difference Tool

	Functions for comparing two data.frames against 
    each other. The core functionality is to provide a detailed breakdown of any differences 
    between two data.frames as well as providing utility functions to help narrow down the 
    source of problems and differences.
	"""
	
	homepage = "https://github.com/gowerc/diffdf"
	cran = "diffdf" 

	version("1.0.4", md5="e03bf42ccf096491fb9b14ac4e64846f")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
