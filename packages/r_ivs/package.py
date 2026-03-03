# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIvs(RPackage):
	"""Interval Vectors

	Provides a library for generic interval manipulations using a
    new interval vector class. Capabilities include: locating various
    kinds of relationships between two interval vectors, merging overlaps
    within a single interval vector, splitting an interval vector on its
    overlapping endpoints, and applying set theoretical operations on
    interval vectors. Many of the operations in this package were inspired
    by James Allen's interval algebra, Allen (1983)
    <doi:10.1145/182.358434>.
	"""
	
	homepage = "https://github.com/DavisVaughan/ivs"
	cran = "ivs" 

	version("0.2.0", md5="217b0c8ed717b1a78490786719a448f4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-glue@1.6.2:", type=("build", "run"))
	depends_on("r-lifecycle@1.0.3:", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-vctrs@0.6:", type=("build", "run"))
