# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowploidydata(RPackage):
	"""Example Flow Cytometry Data

	A collection of raw flow cytometry data for use in vignettes for the flowPloidy package.
	"""
	
	bioc = "flowPloidyData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/flowPloidyData_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/flowPloidyData/flowPloidyData_1.28.0.tar.gz"]

	version("1.28.0", md5="993a663f6d1cdc791c3f4e88d5b3b047")


	# experiment