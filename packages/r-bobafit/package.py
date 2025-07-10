# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBobafit(RPackage):
	"""Refitting diploid region profiles using a clustering procedure

	This package provides a method to refit and correct the diploid region in copy number profiles. It uses a clustering algorithm to identify pathology-specific normal (diploid) chromosomes and then use their copy number signal to refit the whole profile.  The package is composed by three functions: DRrefit (the main function), ComputeNormalChromosome and PlotCluster.
	"""
	
	homepage = "https://github.com/andrea-poletti-unibo/BOBaFIT"
	bioc = "BOBaFIT" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/BOBaFIT_1.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/BOBaFIT/BOBaFIT_1.6.0.tar.gz"]

	version("1.6.0", sha256="111aff16b4d9615fca6db51253ebb997ec54c98e5edec2ab5a8bbe309c033ac1")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-nbclust", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggbio", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-plyranges", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
