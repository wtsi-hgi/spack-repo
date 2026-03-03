# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIpac(RPackage):
	"""Identification of Protein Amino acid Clustering

	iPAC is a novel tool to identify somatic amino acid mutation clustering within proteins while taking into account protein structure.
	"""
	
	bioc = "iPAC" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/iPAC_1.46.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/iPAC/iPAC_1.46.0.tar.gz"]

	version("1.46.0", md5="2ea1fca8a80c62d82be0ef8d6313e52b")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-gdata", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-multtest", type=("build", "run"))
