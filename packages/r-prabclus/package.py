# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrabclus(RPackage):
	"""Functions for Clustering of Presence-Absence, Abundance and Multilocus
	Genetic Data.

	Distance-based parametric bootstrap tests for clustering with  spatial
	neighborhood information. Some distance measures,  Clustering of
	presence-absence, abundance and multilocus genetic data  for species
	delimitation, nearest neighbor  based noise detection. Genetic distances
	between communities. Tests whether various distance-based regressions are
	equal. Try package?prabclus for on overview."""

	cran = "prabclus"

	license("GPL-2.0-or-later")

	version("2.3-3", md5="a978397e43f43298a994a0c8fcc450c7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
