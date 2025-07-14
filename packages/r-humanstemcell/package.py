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

	version("0.48.0", commit="8f4deadb5b277111b26c13ee38dd95870efb5c42")
	version("0.42.0", commit="9c65ba53b1dee0523b67a155b4dc1131edc1f9f4")

	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-hgu133plus2-db", type=("build", "run"))

