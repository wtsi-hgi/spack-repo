# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPinsplus(RPackage):
	"""Clustering Algorithm for Data Integration and Disease Subtyping

	Provides a robust approach for omics data integration and disease subtyping. PINSPlus is fast and supports the analysis of large datasets with hundreds of thousands of samples and features. The software automatically determines the optimal number of clusters and then partitions the samples in a way such that the results are robust against noise and data perturbation (Nguyen et al. (2019) <DOI: 10.1093/bioinformatics/bty1049>, Nguyen et al. (2017)<DOI: 10.1101/gr.215129.116>, Nguyen et al. (2021)<DOI: 10.3389/fonc.2021.725133>).
	"""
	
	cran = "PINSPlus" 

	version("2.0.6", md5="517ba25a9944f6d84d3aceb2fd799ddd")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-entropy", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
