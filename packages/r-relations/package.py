# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRelations(RPackage):
	"""Data Structures and Algorithms for Relations

	Data structures and algorithms for k-ary relations with
  arbitrary domains, featuring relational algebra, predicate functions,
  and fitters for consensus relations.
	"""
	
	cran = "relations" 

	version("0.6-13", md5="5c0e82a37c8f7fb8b74bb5a7ad7fd257")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
	depends_on("r-sets@1.0.16:", type=("build", "run"))
