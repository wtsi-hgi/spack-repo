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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/biotmleData_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/biotmleData/biotmleData_1.26.0.tar.gz"]

	version("1.26.0", md5="8c725d5c496f9bfe7ed4b5d5c538244a")

	depends_on("r@3.5:", type=("build", "run"))

