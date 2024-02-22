# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMulset(RPackage):
	"""Multiset Intersection Generator

	Computes efficient data distributions from highly inconsistent datasets with many missing values using multi-set intersections. Based upon hash functions, 'mulset' can quickly identify intersections from very large matrices of input vectors across columns and rows and thus provides scalable solution for dealing with missing values. Tomic et al. (2019) <doi:10.1101/545186>.
	"""
	
	homepage = "https://github.com/LogIN-/mulset"
	cran = "mulset" 

	version("1.0.0", md5="6b1c3ba680542757760a34121c543131")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
