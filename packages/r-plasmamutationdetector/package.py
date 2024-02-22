# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlasmamutationdetector(RPackage):
	"""Tumor Mutation Detection in Plasma

	Aims at detecting single nucleotide variation
    (SNV) and insertion/deletion (INDEL) in circulating tumor DNA (ctDNA), used
    as a surrogate marker for tumor, at each base position of an Next Generation
    Sequencing (NGS) analysis. Mutations are assessed by comparing the minor-allele
    frequency at each position to the measured PER in control samples.
	"""
	
	cran = "PlasmaMutationDetector" 

	version("1.7.2", md5="d6f10e96936a204de5a43dabb3ac6a44")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ggplot2@2.2:", type=("build", "run"))
	depends_on("r-genomicranges@1.30:", type=("build", "run"))
	depends_on("r-variantannotation@1.24:", type=("build", "run"))
	depends_on("r-s4vectors@0.16:", type=("build", "run"))
	depends_on("r-rsamtools@1.30:", type=("build", "run"))
	depends_on("r-rtracklayer@1.38:", type=("build", "run"))
	depends_on("r-robustbase@0.92.8:", type=("build", "run"))
	depends_on("r-summarizedexperiment@1.8:", type=("build", "run"))
