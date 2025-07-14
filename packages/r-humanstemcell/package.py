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

	version("0.48.0", tag="RELEASE_3_21")
	version("0.42.0", sha256="e052b836a968eeead75523c365d2a73420121475c8f0b5386bef84379f62dc2f")

	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-hgu133plus2-db", type=("build", "run"))

