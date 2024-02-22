# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPolyhaplotyper(RPackage):
	"""Assignment of Haplotypes Based on SNP Dosages in Diploids and
Polyploids

	Infer the genetic composition of individuals
    in terms of haplotype dosages for a haploblock, based
    on bi-allelic marker dosages, for any ploidy level.
    Reference: Voorrips and Tumino: PolyHaplotyper: haplotyping in polyploids based on bi-allelic marker dosage data.
    Submitted to BMC Bioinformatics (2021).
	"""
	
	cran = "PolyHaplotyper" 

	version("1.0.1", md5="5c3467b828e5a5ed7e95e2cbfda5cf94")

	depends_on("r-xml", type=("build", "run"))
