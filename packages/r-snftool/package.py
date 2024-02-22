# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnftool(RPackage):
	"""Similarity Network Fusion

	Similarity Network Fusion takes multiple views of a network and fuses them together to construct an overall status matrix. The input to our algorithm can be feature vectors, pairwise distances, or pairwise similarities. The learned status matrix can then be used for retrieval, clustering, and classification.
	"""
	
	cran = "SNFtool" 

	version("2.3.1", md5="81d3543e0feae4cd1b47b51023e5b8f9")

	depends_on("r-exposition", type=("build", "run"))
	depends_on("r-alluvial", type=("build", "run"))
