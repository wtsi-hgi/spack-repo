# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpicontacts(RPackage):
	"""Handling, Visualisation and Analysis of Epidemiological Contacts

	A collection of tools for representing epidemiological contact data, composed of case line lists and contacts between cases. Also contains procedures for data handling, interactive graphics, and statistics.
	"""
	
	homepage = "https://www.repidemicsconsortium.org/epicontacts/"
	cran = "epicontacts" 

	version("1.1.3", md5="2ab78692efc57cd9fba1205a31504f8d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-threejs", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
