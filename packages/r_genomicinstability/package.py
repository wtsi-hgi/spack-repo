# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenomicinstability(RPackage):
	"""Genomic Instability estimation for scRNA-Seq

	This package contain functions to run genomic instability analysis (GIA) from scRNA-Seq data. GIA estimates the association between gene expression and genomic location of the coding genes. It uses the aREA algorithm to quantify the enrichment of sets of contiguous genes (loci-blocks) on the gene expression profiles and estimates the Genomic Instability Score (GIS) for each analyzed cell.
	"""
	
	homepage = "https://github.com/DarwinHealth/genomicInstability"
	bioc = "genomicInstability" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/genomicInstability_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/genomicInstability/genomicInstability_1.8.0.tar.gz"]

	version("1.8.0", md5="0d7c244a904ea9286d4e965cddeaf2d7")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-mixtools", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
