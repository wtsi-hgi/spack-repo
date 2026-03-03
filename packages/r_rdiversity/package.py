# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdiversity(RPackage):
	"""Measurement and Partitioning of Similarity-Sensitive
Biodiversity

	Provides a framework for the measurement and partitioning of
    the (similarity-sensitive) biodiversity of a metacommunity and its
    constituent subcommunities. Richard Reeve, et al. (2016) 
    <arXiv:1404.6520v3>.
	"""
	
	homepage = "https://github.com/boydorr/rdiversity"
	cran = "rdiversity" 

	version("2.2.0", md5="01275738ec69347ff88ce21f8065d8fb")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
