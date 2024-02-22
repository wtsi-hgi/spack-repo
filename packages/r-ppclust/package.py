# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPpclust(RPackage):
	"""Probabilistic and Possibilistic Cluster Analysis

	Partitioning clustering divides the objects in a data set into non-overlapping subsets or clusters by using the prototype-based probabilistic and possibilistic clustering algorithms. This package covers a set of the functions for Fuzzy C-Means (Bezdek, 1974) <doi:10.1080/01969727308546047>, Possibilistic C-Means (Krishnapuram & Keller, 1993) <doi:10.1109/91.227387>, Possibilistic Fuzzy C-Means (Pal et al, 2005) <doi:10.1109/TFUZZ.2004.840099>, Possibilistic Clustering Algorithm (Yang et al, 2006) <doi:10.1016/j.patcog.2005.07.005>, Possibilistic C-Means with Repulsion (Wachs et al, 2006) <doi:10.1007/3-540-31662-0_6> and the other variants of hard and soft clustering algorithms. The cluster prototypes and membership matrices required by these partitioning algorithms are initialized with different initialization techniques that are available in the package 'inaparc'. As the distance metrics, not only the Euclidean distance but also a set of the commonly used distance metrics are available to use with some of the algorithms in the package. 
	"""
	
	cran = "ppclust" 

	version("1.1.0.1", md5="d309ebadd595b3ea7e1bf68d0697ec2c")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-inaparc", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
