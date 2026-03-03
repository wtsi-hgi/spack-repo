# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRapidpolygonlookup(RPackage):
	"""POLYGON LOOKUP USING KD TREES

	Facilitates efficient polygon search using kd trees.
    Coordinate level spatial data can be aggregated to higher geographical
    identities like census blocks, ZIP codes or police district boundaries.
    This process requires mapping each point in the given data set to a
    particular identity of the desired geographical hierarchy. Unless efficient
    data structures are used, this can be a daunting task. The operation
    point.in.polygon() from the package sp is computationally expensive.
    Here, we exploit kd-trees as efficient nearest neighbor search algorithm
    to dramatically reduce the effective number of polygons being searched.
	"""
	
	cran = "RapidPolygonLookup" 

	version("0.1.1", md5="b7cece6ee5a4a19790ecee9f7ff4464f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-pbsmapping", type=("build", "run"))
	depends_on("r-rgooglemaps", type=("build", "run"))
