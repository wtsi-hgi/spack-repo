# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowsortedCordblood450k(RPackage):
	"""Illumina 450k data on sorted cord blood cells

	Raw data objects to be used for cord blood cell proportion estimation in minfi.
	"""
	
	bioc = "FlowSorted.CordBlood.450k"

	version("1.36.0", commit="48e016cbdacdb6c1e24da59799b58ada13cb2c8e")
	version("1.30.0", commit="260dcd8d87b014827f8178abbe19e046b06ac5d4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-minfi@1.21.2:", type=("build", "run"))

