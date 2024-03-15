# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMinfidataepic(RPackage):
	"""Example data for the Illumina Methylation EPIC array

	Data from 3 technical replicates of the cell line GM12878 from the EPIC methylation array.
	"""
	
	bioc = "minfiDataEPIC" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/minfiDataEPIC_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/minfiDataEPIC/minfiDataEPIC_1.28.0.tar.gz"]

	version("1.28.0", md5="bcb0b01d571c5308e02db4c6b5c0d1ce")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-minfi@1.21.2:", type=("build", "run"))
	depends_on("r-illuminahumanmethylationepicmanifest", type=("build", "run"))
	depends_on("r-illuminahumanmethylationepicanno-ilm10b2-hg19", type=("build", "run"))

	# experiment