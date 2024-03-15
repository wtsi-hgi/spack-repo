# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMedme(RPackage):
	"""Modelling Experimental Data from MeDIP Enrichment

	MEDME allows the prediction of absolute and relative methylation levels based on measures obtained by MeDIP-microarray experiments
	"""
	
	bioc = "MEDME" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MEDME_1.62.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MEDME/MEDME_1.62.0.tar.gz"]

	version("1.62.0", md5="03868c2e2f04af9c9f33d48cc6abed08")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-drc", type=("build", "run"))
