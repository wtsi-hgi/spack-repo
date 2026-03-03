# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAquadtree(RPackage):
	"""Confidentiality of Spatial Point Data

	Provides an automatic aggregation tool to manage point data privacy, 
    intended to be helpful for the production of official spatial data and for researchers.
    The package pursues the data accuracy at the smallest possible areas preventing 
    individual information disclosure. The methodology, based on hierarchical geographic 
    data structures performs aggregation and local suppression of point data to ensure privacy
    as described in Lagonigro, R., Oller, R., Martori J.C. (2017) <doi:10.2436/20.8080.02.55>.
    The data structures are created following the guidelines for grid datasets from the
    European Forum for Geography and Statistics. 
	"""
	
	cran = "AQuadtree" 

	version("1.0.4", md5="77fb18e32abbbbc09c58088d9e879602")

	depends_on("r@3.3.2:", type=("build", "run"))
	depends_on("r-sp@2.0.0:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
