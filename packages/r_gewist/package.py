# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGewist(RPackage):
	"""Gene Environment Wide Interaction Search Threshold

	This 'GEWIST' package provides statistical tools to efficiently optimize SNP prioritization for gene-gene and gene-environment interactions.
	"""
	
	bioc = "GEWIST" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GEWIST_1.46.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GEWIST/GEWIST_1.46.0.tar.gz"]

	version("1.46.0", md5="3fe24d9c2f80cfc18dc41b37b118be6e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
