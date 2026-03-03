# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REconullnetr(RPackage):
	"""Null Model Analysis for Ecological Networks

	Tools for using null models to analyse ecological
    networks (e.g. food webs, flower-visitation networks, seed-dispersal
    networks) and detect resource preferences or non-random interactions among
    network nodes. Tools are provided to run null models, test for and plot
    preferences, plot and analyse bipartite networks, and export null model
    results in a form compatible with other network analysis packages. The 
    underlying null model was developed by Agusti et al. (2003) Molecular 
    Ecology <doi:10.1046/j.1365-294X.2003.02014.x> and the full application to 
    ecological networks by Vaughan et al. (2018) econullnetr: an R package 
    using null models to analyse the structure of ecological networks and 
    identify resource selection. Methods in Ecology & Evolution, 
    <doi:10.1111/2041-210X.12907>.
	"""
	
	cran = "econullnetr" 

	version("0.2.1", md5="b49ac200a9f39c01535906201b423254")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-bipartite", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
