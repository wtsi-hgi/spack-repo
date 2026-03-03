# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClusboot(RPackage):
	"""Bootstrap a Clustering Solution to Establish the Stability of
the Clusters

	Providing a cluster allocation for n samples, either with an $n times p$ data matrix or an $n times n$ distance
                matrix, a bootstrap procedure is performed. The proportion of bootstrap replicates where a pair of samples
                cluster in the same cluster indicates who tightly the samples in a particular cluster clusters together.
	"""
	
	cran = "ClusBoot" 

	version("1.2.1", md5="7b2873c51bf79aec6ed98e13079487b9")

	depends_on("r@2.10:", type=("build", "run"))
