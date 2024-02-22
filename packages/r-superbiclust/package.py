# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSuperbiclust(RPackage):
	"""Generating Robust Biclusters from a Bicluster Set (Ensemble
Biclustering)

	Biclusters are submatrices in the data matrix which
        satisfy certain conditions of homogeneity. Package contains
        functions for generating robust biclusters with respect to the
        initialization parameters for a given bicluster solution
        contained in a bicluster set in data, the procedure is also
        known as ensemble biclustering. The set of biclusters is
        evaluated based on the similarity of its elements (the
        overlap), and afterwards the hierarchical tree is constructed
        to obtain cut-off points for the classes of robust biclusters.
        The result is a number of robust (or super) biclusters with
        none or low overlap.
	"""
	
	cran = "superbiclust" 

	version("1.2", md5="8848249a42b2e29fbdb42abe59b4ef9a")

	depends_on("r-biclust", type=("build", "run"))
	depends_on("r-fabia", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
