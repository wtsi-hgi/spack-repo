# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROctadDb(RPackage):
	"""Open Cancer TherApeutic Discovery (OCTAD) database

	Open Cancer TherApeutic Discovery (OCTAD) package implies sRGES approach for the drug discovery. The essential idea is to identify drugs that reverse the gene expression signature of a disease by tamping down over-expressed genes and stimulating weakly expressed ones. The following package contains all required precomputed data for whole OCTAD pipeline computation.
	"""
	
	bioc = "octad.db"

	version("1.10.0", commit="8d8ae172291782d358ad116d19544dcdcc9e520c")
	version("1.4.0", commit="be738ab6db0a21919d799cefd6d72d9b87fa4d3d")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))

