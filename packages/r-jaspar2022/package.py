# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJaspar2022(RPackage):
	"""Data package for JASPAR database (version 2022)

	JASPAR is an open-access database containing manually curated, non-redundant transcription factor (TF) binding profiles for TFs across six taxonomic groups. In this 9th release, we expanded the CORE collection with 341 new profiles (148 for plants, 101 for vertebrates, 85 for urochordates, and 7 for insects), which corresponds to a 19% expansion over the previous release. To search thisdatabases, please use the package TFBSTools (>= 1.31.2).
	"""
	
	homepage = "http://jaspar.genereg.net/"
	bioc = "JASPAR2022"

	version("0.99.8", commit="533a1e06a04ce7287c92bbbce99bb8b01505d4cf")
	version("0.99.7", commit="461272a7e136f69e2b4d3ebac1181132a5ab3a60")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))

