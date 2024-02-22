# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RText2map(RPackage):
	"""R Tools for Text Matrices, Embeddings, and Networks

	This is a collection of functions optimized for working with
             with various kinds of text matrices. Focusing on 
             the text matrix as the primary object - represented 
             either as a base R dense matrix or a 'Matrix' package sparse 
             matrix - allows for a consistent and intuitive interface 
             that stays close to the underlying mathematical foundation 
             of computational text analysis. In particular, the package
             includes functions for working with word embeddings, 
             text networks, and document-term matrices. Methods developed in 
             Stoltz and Taylor (2019) <doi:10.1007/s42001-019-00048-6>, 
             Taylor and Stoltz (2020) <doi:10.1007/s42001-020-00075-8>, 
             Taylor and Stoltz (2020) <doi:10.15195/v7.a23>, and
             Stoltz and Taylor (2021) <doi:10.1016/j.poetic.2021.101567>.
	"""
	
	homepage = "https://gitlab.com/culturalcartography/text2map"
	cran = "text2map" 

	version("0.1.8", md5="d26bad592643b7b3368ccb2bb38ac25c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix@1.4.2:", type=("build", "run"))
	depends_on("r-text2vec", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-kit", type=("build", "run"))
	depends_on("r-fastmatch", type=("build", "run"))
	depends_on("r-qgraph@1.6.9:", type=("build", "run"))
	depends_on("r-igraph@1.2.6:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-clusterr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rsvd", type=("build", "run"))
	depends_on("r-permute", type=("build", "run"))
