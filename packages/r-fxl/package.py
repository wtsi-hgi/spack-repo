# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFxl(RPackage):
	"""'fxl' Single Case Design Charting Package

	The 'fxl' Charting package is used to prepare and design single case design figures that are typically prepared in spreadsheet software. With 'fxl', there is no need to leave the R environment to prepare these works.
	"""
	
	cran = "fxl" 

	version("1.6.3", md5="c969ad4b5952129c1f305438def2becd")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-grimport", type=("build", "run"))
