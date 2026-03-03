# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlender(RPackage):
	"""Analyze biotic homogenization of landscapes

	Tools for assessing exotic species' contributions to
        landscape homogeneity using average pairwise Jaccard similarity
        and an analytical approximation derived in Harris et al. (2011,
        "Occupancy is nine-tenths of the law," The American
        Naturalist). Also includes a randomization method for assessing
        sources of model error.
	"""
	
	cran = "blender" 

	version("0.1.2", md5="580b157c4f7b6af6dd5884ccf8f30322")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
