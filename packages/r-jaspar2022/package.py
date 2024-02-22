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
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/JASPAR2022_0.99.7.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/JASPAR2022/JASPAR2022_0.99.7.tar.gz"]

	version("0.99.7", md5="282af23228198a377fa9bd76c94dd5eb", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/JASPAR2022_0.99.7.tar.gz")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))

	# annotation