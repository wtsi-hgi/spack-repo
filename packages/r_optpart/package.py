# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptpart(RPackage):
	"""Optimal Partitioning of Similarity Relations

	Contains a set of algorithms for creating
        partitions and coverings of objects largely based on operations
        on (dis)similarity relations (or matrices). There are several
        iterative re-assignment algorithms optimizing different
        goodness-of-clustering criteria.  In addition, there are
        covering algorithms 'clique' which derives maximal cliques, and
        'maxpact' which creates a covering of maximally compact sets.
        Graphical analyses and conversion routines are also included.
	"""
	
	homepage = "http://ecology.msu.montana.edu/labdsv/R"
	cran = "optpart" 

	version("3.0-3", md5="ef87f178acbe3258739bf2b9bbd521ef")

	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-labdsv", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
