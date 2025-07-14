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

	version("1.34.0", tag="RELEASE_3_21")
	version("1.28.0", sha256="01a66a184ce552c2742c71fb7d34c0f1af9c78ad6043f68eac374a201a427ce4")


