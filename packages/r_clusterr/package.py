# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClusterr(RPackage):
	"""Gaussian Mixture Models, K-Means, Mini-Batch-Kmeans, K-Medoids
and Affinity Propagation Clustering

	Gaussian mixture models, k-means, mini-batch-kmeans, k-medoids and affinity propagation clustering with the option to plot, validate, predict (new data) and estimate the optimal number of clusters. The package takes advantage of 'RcppArmadillo' to speed up the computationally intensive parts of the functions. For more information, see (i) "Clustering in an Object-Oriented Environment" by Anja Struyf, Mia Hubert, Peter Rousseeuw (1997), Journal of Statistical Software, <doi:10.18637/jss.v001.i04>; (ii) "Web-scale k-means clustering" by D. Sculley (2010), ACM Digital Library, <doi:10.1145/1772690.1772862>; (iii) "Armadillo: a template-based C++ library for linear algebra" by Sanderson et al (2016), The Journal of Open Source Software, <doi:10.21105/joss.00026>; (iv) "Clustering by Passing Messages Between Data Points" by Brendan J. Frey and Delbert Dueck, Science 16 Feb 2007: Vol. 315, Issue 5814, pp. 972-976, <doi:10.1126/science.1136800>.
	"""
	
	homepage = "https://github.com/mlampros/ClusterR"
	cran = "ClusterR" 

	version("1.3.2", md5="db4df3783599b89771fe88f0de8bf509")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-gmp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.9.1:", type=("build", "run"))
	depends_on("lapack", type=("build", "link", "run"))
	depends_on("gcc", type=("build", "link", "run"))
	depends_on("gmp", type=("build", "link", "run"))
