# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIgraphdata(RPackage):
	"""A Collection of Network Data Sets for the 'igraph' Package

	A small collection of various network data sets,
    to use with the 'igraph' package: the Enron email network, various food webs,
    interactions in the immunoglobulin protein, the karate club network,
    Koenigsberg's bridges, visuotactile brain areas of the macaque monkey,
    UK faculty friendship network, domestic US flights network, etc.
	"""
	
	homepage = "http://igraph.org"
	cran = "igraphdata" 

	version("1.0.1", md5="1098306b9386113ce33ad00212828663")

	depends_on("r@2.10:", type=("build", "run"))
