# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcxn(RPackage):
	"""Exploring, analyzing and visualizing functions utilizing the pcxnData package

	Discover the correlated pathways/gene sets of a single pathway/gene set or discover correlation relationships among multiple pathways/gene sets. Draw a heatmap or create a network of your query and extract members of each pathway/gene set found in the available collections (MSigDB H hallmark, MSigDB C2 Canonical pathways, MSigDB C5 GO BP and Pathprint).
	"""
	
	bioc = "pcxn" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/pcxn_2.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/pcxn/pcxn_2.24.0.tar.gz"]

	version("2.24.0", sha256="27d69bfec32c44871df38b45e3d251a102aa40c9dbc04c640d2cbf33d7d01bd5")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-pcxndata", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
