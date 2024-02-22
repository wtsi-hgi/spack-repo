# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFcmapper(RPackage):
	"""Fuzzy Cognitive Mapping

	Provides several functions to create and manipulate fuzzy
    cognitive maps. It is based on 'FCMapper' for Excel, distributed at <http://
    www.fcmappers.net/joomla/>, developed by Michael Bachhofer and Martin Wildenberg.
    Maps are inputted as adjacency matrices. Attributes of the maps and the
    equilibrium values of the concepts (including with user-defined constrained
    values) can be calculated. The maps can be graphed with a function that calls
    'igraph'. Multiple maps with shared concepts can be aggregated.
	"""
	
	cran = "FCMapper" 

	version("1.1", md5="1fa3633b611d46a13331f764cbf2ca86")

	depends_on("r-igraph", type=("build", "run"))
