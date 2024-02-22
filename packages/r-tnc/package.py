# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTnc(RPackage):
	"""Temporal Network Centrality (TNC) Measures

	Node centrality measures for temporal networks. Available measures are temporal degree centrality, temporal closeness centrality and temporal betweenness centrality defined by Kim and Anderson (2012) <doi:10.1103/PhysRevE.85.026107>. Applying the REN algorithm by Hanke and Foraita (2017) <doi:10.1186/s12859-017-1677-x> when calculating the centrality measures keeps the computational running time linear in the number of graph snapshots. Further, all methods can run in parallel up to the number of nodes in the network.
	"""
	
	cran = "TNC" 

	version("0.1.0", md5="e87510a7944b484d38cae982a685a087")

	depends_on("r@3.4.1:", type=("build", "run"))
