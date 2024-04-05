# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMugaexampledata(RPackage):
	"""Example {M}ouse {U}niversal {G}enotyping {A}rray data for genome reconstruction and quantitative trait locus mapping.

	This package contains example data for the MUGA array that is used by the R package DOQTL.
	"""
	
	bioc = "MUGAExampleData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/MUGAExampleData_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/MUGAExampleData/MUGAExampleData_1.22.0.tar.gz"]

	version("1.22.0", md5="b7fe2c7ad41486695fb78263a8c9a854")

	depends_on("r@2.10:", type=("build", "run"))

