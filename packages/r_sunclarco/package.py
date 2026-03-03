# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSunclarco(RPackage):
	"""Survival Analysis using Copulas

	Survival analysis for unbalanced clusters using Archimedean copulas (Prenen et al. (2016) <DOI:10.1111/rssb.12174>).
	"""
	
	cran = "Sunclarco" 

	version("1.0.0", md5="08c7da3fb37de01dcb44f1f6ba385351")

	depends_on("r-survival", type=("build", "run"))
