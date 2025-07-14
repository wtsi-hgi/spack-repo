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

    version("1.28.0", tag="RELEASE_3_21")
	version("1.22.0", sha256="388388e93786ebea27da4ac2005026f85379e7c7fea05d6bad3e92c02ec60be1")

	depends_on("r@2.10:", type=("build", "run"))

