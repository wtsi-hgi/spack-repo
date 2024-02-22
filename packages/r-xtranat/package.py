# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXtranat(RPackage):
	"""Network Metrics Based on Random Walks

	There are two new network metrics, RWC (random walk centrality) and CBET (counting betweenness). Also available are the normalized versions of those metrics. These measures of centrality and betweenness are particularly useful for the analysis of very dense weighted networks which include loops. Traditional measures do not work as well for those network characteristics. The main reference is DePaolis at al (2022) <doi:10.1007/s41109-022-00519-2>.
	"""
	
	homepage = "https://github.com/fdepaolis/xtranat"
	cran = "xtranat" 

	version("0.1.0", md5="d7460dd234c4eb0c7311a9af4312fd49")

	depends_on("r@2.10:", type=("build", "run"))
