# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFluidigm(RPackage):
	"""Handling Fluidigm Data

	Designed to streamline the process of analyzing genotyping data from Fluidigm machines, this package offers a suite of tools for data handling and analysis. It includes functions for converting Fluidigm data to format used by 'PLINK', estimating errors, calculating pairwise similarities, determining pairwise similarity loci, and generating a similarity matrix.
	"""
	
	cran = "Fluidigm" 

	version("0.2", md5="a58c6904808a5613c1402003c5637624")

	depends_on("r-data-table@1.9.4:", type=("build", "run"))
	depends_on("r-reshape@0.8.8:", type=("build", "run"))
	depends_on("perl@5.10:", type=("build", "link", "run"))
	depends_on("plink@1.07:", type=("build", "link", "run"))
