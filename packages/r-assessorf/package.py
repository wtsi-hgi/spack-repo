# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAssessorf(RPackage):
	"""Assess Gene Predictions Using Proteomics and Evolutionary Conservation

	In order to assess the quality of a set of predicted genes for a genome, evidence must first be mapped to that genome. Next, each gene must be categorized based on how strong the evidence is for or against that gene. The AssessORF package provides the functions and class structures necessary for accomplishing those tasks, using proteomic hits and evolutionarily conserved start codons as the forms of evidence.
	"""
	
	bioc = "AssessORF" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/AssessORF_1.20.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/AssessORF/AssessORF_1.20.0.tar.gz"]

	version("1.20.0", md5="b11ca260fff21c6afe98ee471d79b3ec")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-decipher@2.10:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
