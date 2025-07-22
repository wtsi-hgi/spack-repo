# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBeadarraysnp(RPackage):
	"""Normalization and reporting of Illumina SNP bead arrays

	Importing data from Illumina SNP experiments and performing copy number calculations and reports.
	"""
	
	bioc = "beadarraySNP" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/beadarraySNP_1.68.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/beadarraySNP/beadarraySNP_1.68.0.tar.gz"]

	version("1.68.0", sha256="fafee5b78dc49205f8d252cb65aa91324897e1851d83389fe061ffeb0efc31ef")

	depends_on("r-biobase@2.14:", type=("build", "run"))
	depends_on("r-quantsmooth", type=("build", "run"))
