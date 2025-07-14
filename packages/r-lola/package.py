# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLola(RPackage):
	"""Locus overlap analysis for enrichment of genomic ranges

	Provides functions for testing overlap of sets of genomic regions with public and custom region set (genomic ranges) databases. This makes it possible to do automated enrichment analysis for genomic region sets, thus facilitating interpretation of functional genomics and epigenomics data.
	"""
	
	homepage = "http://code.databio.org/LOLA"
	bioc = "LOLA" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/LOLA_1.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/LOLA/LOLA_1.32.0.tar.gz"]

    version("1.38.0", tag="RELEASE_3_21")
	version("1.32.0", sha256="0ccb4fc00c439dbefdce5ded22d5e2b3df5c89885bae866012c640c6fd0a6c70")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
