# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROligodata(RPackage):
	"""Dataset samples for the oligo package

	Dataset samples (Affymetrix: Expression, Gene, Exon, SNP; NimbleGen: Expression, Tiling) to be used with the oligo package.
	"""
	
	bioc = "oligoData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/oligoData_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/oligoData/oligoData_1.8.0.tar.gz"]

	version("1.8.0", sha256="1e593c1e45c81b428f6edd0e3e751932cbc8bb47d0f65284264c6c3974753eb4")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-oligo", type=("build", "run"))

