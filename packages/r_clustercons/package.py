# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClustercons(RPackage):
	"""Consensus Clustering using Multiple Algorithms and Parameters

	Functions for calculation of robustness measures for clusters and cluster membership based on generating consensus matrices from bootstrapped clustering experiments in which a random proportion of rows of the data set are used in each individual clustering. This allows the user to prioritise clusters and the members of clusters based on their consistency in this regime. The functions allow the user to select several algorithms to use in the re-sampling scheme and with any of the parameters that the algorithm would normally take. See Simpson, T. I., Armstrong, J. D. & Jarman, A. P. (2010) <doi:10.1186/1471-2105-11-590> and Monti, S., Tamayo, P., Mesirov, J. & Golub, T. (2003) <doi:10.1023/a:1023949509487>.
	"""
	
	homepage = "https://github.com/biomedicalinformaticsgroup/clusterCons"
	cran = "clusterCons" 

	version("1.2", md5="fc9dc671ef0e4e5574a319bd1bca10c4")

	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-apcluster", type=("build", "run"))
