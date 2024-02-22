# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REntrymodels(RPackage):
	"""Estimate Entry Models

	Tools for measuring empirically the effects of entry in concentrated markets, based in Bresnahan and Reiss (1991) <https://www.jstor.org/stable/2937655>. 
	"""
	
	cran = "entrymodels" 

	version("0.2.1", md5="7d4651300c229975d7f7aaf2d498fcb1")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
