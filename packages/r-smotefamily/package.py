# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmotefamily(RPackage):
	"""A Collection of Oversampling Techniques for Class Imbalance
Problem Based on SMOTE

	A collection of various oversampling techniques developed from SMOTE is provided. SMOTE is a oversampling technique which synthesizes a new minority instance between a pair of one minority instance and one of its K nearest neighbor. (see <https://www.jair.org/media/953/live-953-2037-jair.pdf> for more information) Other techniques adopt this concept with other criteria in order to generate balanced dataset for class imbalance problem.
	"""
	
	cran = "smotefamily" 

	version("1.3.1", md5="15fa13b0078567d5339efa7d6a288f81")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-dbscan", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
