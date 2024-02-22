# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatasetsLoad(RPackage):
	"""Graphical Interface for Loading Datasets

	Graphical interface for loading datasets in RStudio from all installed (including unloaded) packages, also includes command line interfaces.
	"""
	
	cran = "datasets.load" 

	version("2.3.0", md5="619215ab3677e0a7c25cd6bb91823c87")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
