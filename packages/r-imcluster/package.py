# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImcluster(RPackage):
	"""Efficiency of Cluster Sampling for Crop Surveys

	Cluster sampling is a valuable approach when constructing a comprehensive list of individual units is challenging. It provides operational and cost advantages. This package is designed to test the efficiency of cluster sampling in terms cluster variance and design effect in context to crop surveys. This package has been developed using the algorithm of Iqbal et al. (2018) <doi:10.19080/BBOAJ.2018.05.555673>.
	"""
	
	cran = "ImCluster" 

	version("0.1.0", md5="146534185270e1b82ab3f23cbb982b71")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
