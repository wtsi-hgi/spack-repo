# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKselection(RPackage):
	"""Selection of K in K-Means Clustering

	Selection of k in k-means clustering based on Pham et al. paper
    ``Selection of k in k-means clustering''.
	"""
	
	homepage = "https://github.com/drodriguezperez/kselection"
	cran = "kselection" 

	version("0.2.1", md5="a26f5f7043301613576b5d95009593d1")

