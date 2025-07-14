# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSevenc(RPackage):
	"""Computational Chromosome Conformation Capture by Correlation of ChIP-seq at CTCF motifs

	Chromatin looping is an essential feature of eukaryotic genomes and can bring regulatory sequences, such as enhancers or transcription factor binding sites, in the close physical proximity of regulated target genes. Here, we provide sevenC, an R package that uses protein binding signals from ChIP-seq and sequence motif information to predict chromatin looping events. Cross-linking of proteins that bind close to loop anchors result in ChIP-seq signals at both anchor loci. These signals are used at CTCF motif pairs together with their distance and orientation to each other to predict whether they interact or not. The resulting chromatin loops might be used to associate enhancers or transcription factor binding sites (e.g., ChIP-seq peaks) to regulated target genes.
	"""
	
	homepage = "https://github.com/ibn-salem/sevenC"
	bioc = "sevenC" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/sevenC_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/sevenC/sevenC_1.22.0.tar.gz"]

	version("1.28.0", tag="RELEASE_3_21")
	version("1.22.0", sha256="82d883995a13847cd7139af0639d5d399679cf290db412fc8425028c8ed13acd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-interactionset@1.2:", type=("build", "run"))
	depends_on("r-rtracklayer@1.34.1:", type=("build", "run"))
	depends_on("r-biocgenerics@0.22:", type=("build", "run"))
	depends_on("r-genomeinfodb@1.12.2:", type=("build", "run"))
	depends_on("r-genomicranges@1.28.5:", type=("build", "run"))
	depends_on("r-iranges@2.10.3:", type=("build", "run"))
	depends_on("r-s4vectors@0.14.4:", type=("build", "run"))
	depends_on("r-readr@1.1:", type=("build", "run"))
	depends_on("r-purrr@0.2.2:", type=("build", "run"))
	depends_on("r-data-table@1.10.4:", type=("build", "run"))
	depends_on("r-boot@1.3.20:", type=("build", "run"))
