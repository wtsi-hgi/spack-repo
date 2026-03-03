# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoots(RPackage):
	"""Reconstructing Ordered Ontogenic Trajectories

	A set of tools to reconstruct ordered ontogenic trajectories from
    single cell RNAseq data.
	"""
	
	cran = "roots" 

	version("1.0", md5="780607f07fd04914d4fb8556dd7089c5")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-animation@2.4:", type=("build", "run"))
	depends_on("r-rarpack@0.11.0:", type=("build", "run"))
	depends_on("r-igraph@1:", type=("build", "run"))
