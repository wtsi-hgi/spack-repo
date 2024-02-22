# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparsefunclust(RPackage):
	"""Sparse Functional Clustering

	Provides a general framework for performing sparse functional
    clustering as originally described in Floriello and Vitelli (2017)
    <doi:10.1016/j.jmva.2016.10.008>, with the possibility of jointly handling
    data misalignment (see Vitelli, 2019, <doi:10.48550/arXiv.1912.00687>).
	"""
	
	cran = "SparseFunClust" 

	version("1.0.0", md5="acca41dd19c853f8996d7a91f3d8b0c3")

	depends_on("r-cluster", type=("build", "run"))
