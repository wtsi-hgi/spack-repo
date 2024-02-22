# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClustergeneration(RPackage):
	"""Random Cluster Generation (with Specified Degree of Separation).

	We developed the clusterGeneration package to provide functions  for
	generating random clusters, generating random  covariance/correlation
	matrices, calculating a separation index (data and population version) for
	pairs of clusters or cluster distributions, and 1-D and 2-D projection
	plots to visualize clusters.  The package also contains a function to
	generate random clusters based on factorial designs with factors such as
	degree of separation, number of clusters, number of variables, number of
	noisy variables."""

	cran = "clusterGeneration"

	version("1.3.8", md5="d218d619e9615d747da257e0c7d78b6b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
