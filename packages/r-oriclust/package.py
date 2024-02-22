# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROriclust(RPackage):
	"""Order-Restricted Information Criterion-Based Clustering
Algorithm

	A user-friendly R-based software package for
        gene clustering. Clusters are given by genes matched to
        prespecified profiles across various ordered treatment groups.
        It is particularly useful for analyzing data obtained from
        short time-course or dose-response microarray experiments.
	"""
	
	cran = "ORIClust" 

	version("1.0-2", md5="45f234da67bcf367370cf7b471511f19")

	depends_on("r@2.10:", type=("build", "run"))
