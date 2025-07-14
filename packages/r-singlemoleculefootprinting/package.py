# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSinglemoleculefootprinting(RPackage):
	"""Analysis tools for Single Molecule Footprinting (SMF) data

	SingleMoleculeFootprinting is an R package providing functions to analyze Single Molecule Footprinting (SMF) data. Following the workflow exemplified in its vignette, the user will be able to perform basic data analysis of SMF data with minimal coding effort. Starting from an aligned bam file, we show how to perform quality controls over sequencing libraries, extract methylation information at the single molecule level accounting for the two possible kind of SMF experiments (single enzyme or double enzyme), classify single molecules based on their patterns of molecular occupancy, plot SMF information at a given genomic location
	"""
	
	bioc = "SingleMoleculeFootprinting" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SingleMoleculeFootprinting_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SingleMoleculeFootprinting/SingleMoleculeFootprinting_1.10.0.tar.gz"]

	version("2.2.0", tag="RELEASE_3_21")
	version("1.10.0", sha256="25f5df0e2eb836bc0fc80be1bfab0bb501f24d416199da14c6007b5a458eb096")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-quasr", type=("build", "run"))
