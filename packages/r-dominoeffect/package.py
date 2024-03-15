# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDominoeffect(RPackage):
	"""Identification and Annotation of Protein Hotspot Residues

	The functions support identification and annotation of hotspot residues in proteins. These are individual amino acids that accumulate mutations at a much higher rate than their surrounding regions.
	"""
	
	bioc = "DominoEffect" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/DominoEffect_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/DominoEffect/DominoEffect_1.22.0.tar.gz"]

	version("1.22.0", md5="2e92d099e31b5feaf035b8eb5ad92376")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
