# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClustersignificance(RPackage):
	"""The ClusterSignificance package provides tools to assess if class clusters in dimensionality reduced data representations have a separation different from permuted data

	The ClusterSignificance package provides tools to assess if class clusters in dimensionality reduced data representations have a separation different from permuted data. The term class clusters here refers to, clusters of points representing known classes in the data. This is particularly useful to determine if a subset of the variables, e.g. genes in a specific pathway, alone can separate samples into these established classes. ClusterSignificance accomplishes this by, projecting all points onto a one dimensional line. Cluster separations are then scored and the probability of the seen separation being due to chance is evaluated using a permutation method.
	"""
	
	homepage = "https://github.com/jasonserviss/ClusterSignificance/"
	bioc = "ClusterSignificance" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ClusterSignificance_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ClusterSignificance/ClusterSignificance_1.30.0.tar.gz"]

	version("1.36.0", tag="RELEASE_3_21")
	version("1.30.0", sha256="2401e2c5911cdf942c2f1d771257ef8536875d2c074781dad67fff54cd12dccb")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-princurve@2.0.5:", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
