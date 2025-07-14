# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFishalyser(RPackage):
	"""FISHalyseR a package for automated FISH quantification

	FISHalyseR provides functionality to process and analyse digital cell culture images, in particular to quantify FISH probes within nuclei. Furthermore, it extract the spatial location of each nucleus as well as each probe enabling spatial co-localisation analysis.
	"""
	
	bioc = "FISHalyseR"

	version("1.42.0", commit="a208ea1483a8f57b01a2c11acadf23df35ad1bef")
	version("1.36.0", commit="8e8cce0f2a1f93558a24b620bbd30489b508abfd")

	depends_on("r-ebimage", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
