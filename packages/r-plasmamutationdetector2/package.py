# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlasmamutationdetector2(RPackage):
	"""Tumor Mutation Detection in Plasma using Barcoding

	Aims at detecting single nucleotide variation
    (SNV) and insertion/deletion (INDEL) in circulating tumor DNA (ctDNA), used
    as a surrogate marker for tumor, at each base position of an Next Generation
    Sequencing (NGS) analysis using barcoding. Mutations are assessed by comparing the minor-allele frequency at each position to the measured PER in control samples.
    This package has been used for Kjersti Tjensvoll, Morten Lapin, Bjørnar Gilje, Herish Garresori, Satu Oltedal, Rakel Brendsdal Forthun, Anders Molven, Yves Rozenholc and Oddmund No{o}rdgaard (2022) <https://www.nature.com/articles/s41598-022-09698-5>.
	"""
	
	cran = "PlasmaMutationDetector2" 

	version("1.1.11", md5="7f657b2a339687a9c8be0e246ded3ec8", url="https://cran.r-project.org/src/contrib/PlasmaMutationDetector2_1.1.11.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@2.2:", type=("build", "run"))
	depends_on("r-genomicranges@1.30:", type=("build", "run"))
	depends_on("r-variantannotation@1.24:", type=("build", "run"))
	depends_on("r-s4vectors@0.16:", type=("build", "run"))
	depends_on("r-rsamtools@1.30:", type=("build", "run"))
	depends_on("r-rtracklayer@1.38:", type=("build", "run"))
	depends_on("r-robustbase@0.92.8:", type=("build", "run"))
	depends_on("r-summarizedexperiment@1.8:", type=("build", "run"))
