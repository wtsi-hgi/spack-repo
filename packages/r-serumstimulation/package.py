# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSerumstimulation(RPackage):
	"""serumStimulation is a data package which is used by examples in package pcaGoPromoter

	Contains 13 micro array data results from a serum stimulation experiment
	"""
	
	bioc = "serumStimulation" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/serumStimulation_1.38.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/serumStimulation/serumStimulation_1.38.0.tar.gz"]

	version("1.38.0", md5="4d3f1a4e58f500d7e424eef0b22c05ad")

	depends_on("r@2.10:", type=("build", "run"))

	# experiment