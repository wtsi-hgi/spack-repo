# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDtwumi(RPackage):
	"""Imputation of Multivariate Time Series Based on Dynamic Time
Warping

	Functions to impute large gaps within multivariate time series based on Dynamic Time Warping methods. Gaps of size 1 or inferior to a defined threshold are filled using simple average and weighted moving average respectively. Larger gaps are filled using the methodology provided by Phan et al. (2017) <DOI:10.1109/MLSP.2017.8168165>: a query is built immediately before/after a gap and a moving window is used to find the most similar sequence to this query using Dynamic Time Warping. To lower the calculation time, similar sequences are pre-selected using global features. Contrary to the univariate method (package 'DTWBI'), these global features are not estimated over the sequence containing the gap(s), but a feature matrix is built to summarize general features of the whole multivariate signal. Once the most similar sequence to the query has been identified, the adjacent sequence to this window is used to fill the gap considered. This function can deal with multiple gaps over all the sequences componing the input multivariate signal. However, for better consistency, large gaps at the same location over all sequences should be avoided.
	"""
	
	homepage = "http://mawenzi.univ-littoral.fr/DTWUMI/"
	cran = "DTWUMI" 

	version("1.0", md5="908cfffb3b819d7dffd552152fecd4d1")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-dtw", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-entropy", type=("build", "run"))
	depends_on("r-lsa", type=("build", "run"))
	depends_on("r-dtwbi", type=("build", "run"))
