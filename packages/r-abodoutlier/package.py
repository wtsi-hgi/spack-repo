# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAbodoutlier(RPackage):
	"""Angle-Based Outlier Detection

	Performs angle-based outlier detection on a given dataframe. Three methods are available, a full but slow implementation using all the data that has cubic complexity, a fully randomized one which is way more efficient and another using k-nearest neighbours. These algorithms are specially well suited for high dimensional data outlier detection.
	"""
	
	cran = "abodOutlier" 

	version("0.1", md5="e3782e42842fc893d036bdfb7fd86d91")

	depends_on("r-cluster", type=("build", "run"))
	depends_on("r@3.1.2:", type=("build", "run"))
