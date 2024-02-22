# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastcluster(RPackage):
	"""Fast Hierarchical Clustering Routines for R and 'Python'.

	This is a two-in-one package which provides interfaces to both R and
	'Python'. It implements fast hierarchical, agglomerative clustering
	routines. Part of the functionality is designed as drop-in replacement for
	existing routines: linkage() in the 'SciPy' package
	'scipy.cluster.hierarchy', hclust() in R's 'stats' package, and the
	'flashClust' package. It provides the same functionality with the benefit
	of a much faster implementation. Moreover, there are memory-saving routines
	for clustering of vector data, which go beyond what the existing packages
	provide. For information on how to install the 'Python' files, see the file
	INSTALL in the source distribution."""

	cran = "fastcluster"

	version("1.2.6", md5="252ea997088794972aac679fb6772530")

	depends_on("r@3:", type=("build", "run"))
