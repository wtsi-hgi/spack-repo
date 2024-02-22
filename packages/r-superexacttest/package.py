# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSuperexacttest(RPackage):
	"""Exact Test and Visualization of Multi-Set Intersections

	Identification of sets of objects with shared features is a common operation in all disciplines. Analysis of intersections among multiple sets is fundamental for in-depth understanding of their complex relationships. This package implements a theoretical framework for efficient computation of statistical distributions of multi-set intersections based upon combinatorial theory, and provides multiple scalable techniques for visualizing the intersection statistics. The statistical algorithm behind this package was published in Wang et al. (2015) <doi:10.1038/srep16923>.
	"""
	
	homepage = "https://github.com/mw201608/SuperExactTest/"
	cran = "SuperExactTest" 

	version("1.1.0", md5="20064bd4dda67e579af01a5009ad35f1")

	depends_on("r@3.1:", type=("build", "run"))
