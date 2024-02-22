# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUpmask(RPackage):
	"""Unsupervised Photometric Membership Assignment in Stellar
Clusters

	An implementation of the UPMASK method for performing membership
    assignment in stellar clusters in R. It is prepared to use photometry and
    spatial positions, but it can take into account other types of data. The
    method is able to take into account arbitrary error models, and it is
    unsupervised, data-driven, physical-model-free and relies on as few
    assumptions as possible. The approach followed for membership assessment is
    based on an iterative process, dimensionality reduction, a clustering
    algorithm and a kernel density estimation.
	"""
	
	cran = "UPMASK" 

	version("1.2", md5="a9fecf8119e53aa028dc993af38a9c34")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-dimred", type=("build", "run"))
	depends_on("r-loe", type=("build", "run"))
