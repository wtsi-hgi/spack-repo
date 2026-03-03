# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RText2vec(RPackage):
	"""Modern Text Mining Framework for R

	Fast and memory-friendly tools for text vectorization, topic
    modeling (LDA, LSA), word embeddings (GloVe), similarities. This package
    provides a source-agnostic streaming API, which allows researchers to perform
    analysis of collections of documents which are larger than available RAM. All
    core functions are parallelized to benefit from multicore machines.
	"""
	
	homepage = "http://text2vec.org"
	cran = "text2vec" 

	version("0.6.4", md5="71e42635651e06b3c168064e92fa7589")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-matrix@1.5.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-r6@2.3:", type=("build", "run"))
	depends_on("r-data-table@1.9.6:", type=("build", "run"))
	depends_on("r-rsparse@0.3.3.4:", type=("build", "run"))
	depends_on("r-stringi@1.1.5:", type=("build", "run"))
	depends_on("r-mlapi@0.1:", type=("build", "run"))
	depends_on("r-lgr@0.2:", type=("build", "run"))
	depends_on("r-digest@0.6.8:", type=("build", "run"))
