# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhylotate(RPackage):
	"""Phylogenies with Annotations

	Functions to read and write APE-compatible phylogenetic
  trees in NEXUS and Newick formats, while preserving annotations.
	"""
	
	cran = "phylotate" 

	version("1.3", md5="3c4c0bbcd1e66cdceb2a29421db1ac79")

	depends_on("r@3:", type=("build", "run"))
