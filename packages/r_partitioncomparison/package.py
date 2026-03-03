# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPartitioncomparison(RPackage):
	"""Implements Measures for the Comparison of Two Partitions

	Provides several measures ((dis)similarity, distance/metric,
    correlation, entropy) for comparing two partitions of the same set of
    objects. The different measures can be assigned to three different
    classes: Pair comparison (containing the famous Jaccard and Rand
    indices), set based, and information theory based.
    Many of the implemented measures can be found in
    Albatineh AN, Niewiadomska-Bugaj M and Mihalko D (2006)
    <doi:10.1007/s00357-006-0017-z> and
    Meila M (2007) <doi:10.1016/j.jmva.2006.11.013>.
    Partitions are represented by vectors of class labels which allow a
    straightforward integration with existing clustering algorithms
    (e.g. kmeans()). The package is mostly based on the S4 object system.
	"""
	
	homepage = "https://github.com/KIT-IISM-EM/partitionComparison"
	cran = "partitionComparison" 

	version("0.2.6", md5="5961b0fd368ab600564dd272b2d4883c")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
