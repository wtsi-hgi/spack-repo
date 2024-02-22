# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPartitions(RPackage):
	"""Additive Partitions of Integers

	Additive partitions of integers.  Enumerates the
  partitions, unequal partitions, and restricted partitions of an
  integer; the three corresponding partition functions are also given.
  Set partitions and now compositions and riffle shuffles are
  included.
	"""
	
	homepage = "https://github.com/RobinHankin/partitions"
	cran = "partitions" 

	version("1.10-7", md5="af0a983e17bee8b38b9b4598925e2bfa")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-gmp", type=("build", "run"))
	depends_on("r-polynom", type=("build", "run"))
	depends_on("r-sets", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
