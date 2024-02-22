# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComphclust(RPackage):
	"""Complementary Hierarchical Clustering

	Performs the complementary hierarchical clustering procedure and returns X' (the expected residual matrix) and a vector of the relative gene importances.
	"""
	
	cran = "compHclust" 

	version("1.0-3", md5="24fcabb4da2e83a88515aa3cf12664e8")

