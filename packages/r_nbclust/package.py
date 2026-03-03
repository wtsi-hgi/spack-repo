# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNbclust(RPackage):
	"""Determining the Best Number of Clusters in a Data Set

	It provides 30 indexes for determining the optimal number of clusters in a data set and offers the best clustering scheme from different results to the user. 
	"""
	
	homepage = "https://sites.google.com/site/malikacharrad/research/nbclust-package"
	cran = "NbClust" 

	version("3.0.1", md5="797acb196fb81f0859acd43f08072546")

	depends_on("r@3.1:", type=("build", "run"))
