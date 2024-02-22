# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnscat(RPackage):
	"""Clustering of Categorical Data

	An implementation of the clustering methods of categorical data
    discussed in Amiri, S., Clarke, B., and Clarke, J. (2015). Clustering categorical 
    data via ensembling dissimilarity matrices.  Preprint <arXiv:1506.07930>.
	"""
	
	homepage = "https://github.com/jlp2duke/EnsCat/wiki/How-To-with-Examples"
	cran = "EnsCat" 

	version("1.1", md5="3cd90f39d730683f8d7857f206941568")

	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggdendro", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r@3.3.2:", type=("build", "run"))
