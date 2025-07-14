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

	version("1.34.0", tag="RELEASE_3_21")
	version("1.28.0", sha256="f00a13daab8b797ab4ec6b4b19042a25077378e5826404f5a0526644faa15cd4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-minfi@1.21.2:", type=("build", "run"))
	depends_on("r-illuminahumanmethylationepicmanifest", type=("build", "run"))
	depends_on("r-illuminahumanmethylationepicanno-ilm10b2-hg19", type=("build", "run"))

