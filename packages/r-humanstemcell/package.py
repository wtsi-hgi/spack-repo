# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHumanstemcell(RPackage):
	"""Human Stem Cells time course experiment

	Affymetrix time course experiment on human stem cells (two time points: undifferentiated and differentiated).
	"""
	
	bioc = "humanStemCell" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/humanStemCell_0.42.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/humanStemCell/humanStemCell_0.42.0.tar.gz"]

	version("0.42.0", md5="be6367d8fa19187d644247ed8795eb0e")

	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-hgu133plus2-db", type=("build", "run"))

	# experiment