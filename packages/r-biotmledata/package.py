# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiotmledata(RPackage):
	"""Example experimental microarray data set for the "biotmle" R package

	Microarray data (from the Illumina Ref-8 BeadChips platform) and phenotype-level data from an epidemiological investigation of benzene exposure, packaged using "SummarizedExperiemnt", for use as an example with the "biotmle" R package.
	"""
	
	bioc = "biotmleData"

	version("1.32.0", commit="cf91e5fbf217f56813932507db4b697509784117")
	version("1.26.0", commit="f8c220ee4059590a70645adcf2a62619a493052d")

	depends_on("r@3.5:", type=("build", "run"))

