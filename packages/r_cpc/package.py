# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCpc(RPackage):
	"""Implementation of Cluster-Polarization Coefficient

	Implements cluster-polarization coefficient for measuring distributional
	polarization in single or multiple dimensions, as well as associated functions.
	Contains support for hierarchical clustering, k-means, partitioning around medoids,
	density-based spatial clustering with noise, and manually imposed cluster membership.
	Mehlhaff (forthcoming) <https://imehlhaff.net/files/CPC_note.pdf>.
	"""
	
	homepage = "http://imehlhaff.net/CPC/"
	cran = "CPC" 

	version("2.5.6", md5="ff85aa23f77e2f079d54915352d89b8a")

	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-dbscan", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
