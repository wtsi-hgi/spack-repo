# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSuperpc(RPackage):
	"""Supervised Principal Components

	Does prediction in the case of a censored survival outcome, or a regression outcome, using the "supervised principal component" approach. 'Superpc' is especially useful for high-dimensional data when the number of features p dominates the number of samples n (p >> n paradigm), as generated, for instance, by high-throughput technologies.
	"""
	
	homepage = "http://www-stat.stanford.edu/~tibs/superpc"
	cran = "superpc" 

	version("1.12", md5="255baabc1cd158ab8e05368e06a887e0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
