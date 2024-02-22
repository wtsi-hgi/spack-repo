# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConclust(RPackage):
	"""Pairwise Constraints Clustering

	There are 4 main functions in this package: ckmeans(), lcvqe(), mpckm() and ccls(). They take an unlabeled dataset and two lists of must-link and cannot-link constraints as input and produce a clustering as output.
	"""
	
	cran = "conclust" 

	version("1.1", md5="67539de3b859b336db8121f495ded5dc")

