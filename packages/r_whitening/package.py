# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWhitening(RPackage):
	"""Whitening and High-Dimensional Canonical Correlation Analysis

	Implements the whitening methods (ZCA, PCA, Cholesky,
 ZCA-cor, and PCA-cor) discussed in Kessy, Lewin, and Strimmer (2018)
 "Optimal whitening and decorrelation", <doi:10.1080/00031305.2016.1277159>,
 as well as the whitening approach to canonical correlation analysis allowing
 negative canonical correlations described in Jendoubi and Strimmer (2019)
 "A whitening approach to probabilistic canonical correlation analysis for omics
 data integration", <doi:10.1186/s12859-018-2572-9>. The package also offers
 functions to simulate random orthogonal matrices, compute (correlation) loadings
 and explained variation. It also contains four example data sets (extended UCI 
 wine data, TCGA LUSC data, nutrimouse data, extended pitprops data).
	"""
	
	homepage = "https://strimmerlab.github.io/software/whitening/"
	cran = "whitening" 

	version("1.4.0", md5="a06f149e481c709d835d89a5c285dc99")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-corpcor@1.6.10:", type=("build", "run"))
