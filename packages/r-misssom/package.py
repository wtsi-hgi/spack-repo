# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMisssom(RPackage):
	"""Self-Organizing Maps with Built-in Missing Data Imputation

	The Self-Organizing Maps with Built-in Missing Data Imputation. Missing values are imputed and regularly updated during the online Kohonen algorithm. Our method can be used for data visualisation, clustering or imputation of missing data. It is an extension of the online algorithm of the 'kohonen' package. The method is described
    in the article "Self-Organizing Maps for Exploration of Partially Observed Data and Imputation of Missing Values" by S. Rejeb, C. Duveau, T. Rebafka (2022) <arXiv:2202.07963>.
	"""
	
	cran = "missSOM" 

	version("1.0.1", md5="3e7ed2122dcf48e8ed16f45bf0090479")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-kpodclustr", type=("build", "run"))
