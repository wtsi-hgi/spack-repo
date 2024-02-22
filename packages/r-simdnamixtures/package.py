# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimdnamixtures(RPackage):
	"""Simulate Forensic DNA Mixtures

	Mixed DNA profiles can be sampled according to models for probabilistic genotyping. Peak height variability is modelled using a log normal distribution or a gamma distribution. Sample contributors may be related according to a pedigree.
	"""
	
	cran = "simDNAmixtures" 

	version("1.0.1", md5="ac6f7cc8120ae79a7b01caf0f61df0b5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-pedtools", type=("build", "run"))
