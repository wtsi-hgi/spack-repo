# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMotif2site(RPackage):
	"""Detect binding sites from motifs and ChIP-seq experiments, and compare binding sites across conditions

	Detect binding sites using motifs IUPAC sequence or bed coordinates and ChIP-seq experiments in bed or bam format. Combine/compare binding sites across experiments, tissues, or conditions. All normalization and differential steps are done using TMM-GLM method. Signal decomposition is done by setting motifs as the centers of the mixture of normal distribution curves.
	"""
	
	bioc = "Motif2Site" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Motif2Site_1.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Motif2Site/Motif2Site_1.6.0.tar.gz"]

	version("1.6.0", sha256="04c6adcdc516e572a34c2842cb61b3929b1e9b97458cbd39260d047f874bc568")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-mixtools", type=("build", "run"))
