# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProvenance(RPackage):
	"""Statistical Toolbox for Sedimentary Provenance Analysis

	Bundles a number of established statistical methods to facilitate the visual interpretation of large datasets in sedimentary geology. Includes functionality for adaptive kernel density estimation, principal component analysis, correspondence analysis, multidimensional scaling, generalised procrustes analysis and individual differences scaling using a variety of dissimilarity measures. Univariate provenance proxies, such as single-grain ages or (isotopic) compositions are compared with the Kolmogorov-Smirnov, Kuiper, Wasserstein-2 or Sircombe-Hazelton L2 distances. Categorical provenance proxies such as chemical compositions are compared with the Aitchison and Bray-Curtis distances,and count data with the chi-square distance. Varietal data can either be converted to one or more distributional datasets, or directly compared using the multivariate Wasserstein distance. Also included are tools to plot compositional and count data on ternary diagrams and point-counting data on radial plots, to calculate the sample size required for specified levels of statistical precision, and to assess the effects of hydraulic sorting on detrital compositions. Includes an intuitive query-based user interface for users who are not proficient in R.
	"""
	
	homepage = "https://www.ucl.ac.uk/~ucfbpve/provenance/"
	cran = "provenance" 

	version("4.2", md5="a32dfc11ea2a50c906194bff73329f7e")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-isoplotr@5.2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
