# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlmts(RPackage):
	"""Machine Learning Algorithms for Multivariate Time Series

	An implementation of several machine learning algorithms for 
    multivariate time series. The package includes functions allowing the
    execution of clustering, classification or outlier detection methods,
    among others. It also incorporates a collection of multivariate time
    series datasets which can be used to analyse the performance of new
    proposed algorithms. Some of these datasets are stored in GitHub data
    packages 'ueadata1' to 'ueadata8'. To access these data packages, run
    'install.packages(c('ueadata1', 'ueadata2', 'ueadata3', 'ueadata4', 'ueadata5', 'ueadata6', 'ueadata7', 'ueadata8'), repos='<https://anloor7.github.io/drat/>')'.
    The installation takes a couple of minutes but we strongly encourage the
    users to do it if they want to have available all datasets of mlmts.
    Practitioners from a broad variety of fields could
    benefit from the general framework provided by 'mlmts'.
	"""
	
	cran = "mlmts" 

	version("1.1.1", md5="6a90f5806f0ac262a0a20fe8af344c48")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-quantspec", type=("build", "run"))
	depends_on("r-waveslim", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-tsclust", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
	depends_on("r-tsa", type=("build", "run"))
	depends_on("r-tsfeatures", type=("build", "run"))
	depends_on("r-tserieschaos", type=("build", "run"))
	depends_on("r-freqdom", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-dtw", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-complexplus", type=("build", "run"))
	depends_on("r-mts", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-multiwave", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-fda-usc", type=("build", "run"))
	depends_on("r-tsdist", type=("build", "run"))
	depends_on("r-geigen", type=("build", "run"))
	depends_on("r-desctools", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-pspline", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-clusterr", type=("build", "run"))
	depends_on("r-aid", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
