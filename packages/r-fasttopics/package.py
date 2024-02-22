# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFasttopics(RPackage):
	"""Fast Algorithms for Fitting Topic Models and Non-Negative Matrix
Factorizations to Count Data

	Implements fast, scalable optimization algorithms for
    fitting topic models ("grade of membership" models) and
    non-negative matrix factorizations to count data. The methods
    exploit the special relationship between the multinomial topic
    model (also, "probabilistic latent semantic indexing") and Poisson
    non-negative matrix factorization. The package provides tools to
    compare, annotate and visualize model fits, including functions to
    efficiently create "structure plots" and identify key features in
    topics. The 'fastTopics' package is a successor to the 'CountClust'
    package. Note that the 'fastTopicis' package on GitHub has more 
    vignettes illustrating application to single-cell RNA-seq data.
	"""
	
	homepage = "https://github.com/stephenslab/fastTopics"
	cran = "fastTopics" 

	version("0.6-163", md5="e3c3a9c8b26ab8eadc799faada06c496")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-uwot", type=("build", "run"))
	depends_on("r-ashr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-ggrepel@0.9:", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
