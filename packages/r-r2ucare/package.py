# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR2ucare(RPackage):
	"""Goodness-of-Fit Tests for Capture-Recapture Models

	Performs goodness-of-fit tests for capture-recapture models as 
    described by Gimenez et al. (2018) <doi:10.1111/2041-210X.13014>. 
    Also contains several functions to process capture-recapture data.
	"""
	
	homepage = "https://github.com/oliviergimenez/R2ucare"
	cran = "R2ucare" 

	version("1.0.2", md5="2a55210f913c8d0c495ce5f47861a304")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rmark", type=("build", "run"))
