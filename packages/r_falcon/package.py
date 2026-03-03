# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFalcon(RPackage):
	"""Finding Allele-Specific Copy Number in Next-Generation
Sequencing Data

	This is a method for Allele-specific DNA Copy Number Profiling using Next-Generation Sequencing.  Given the allele-specific coverage at the variant loci, this program segments the genome into regions of homogeneous allele-specific copy number.  It requires, as input, the read counts for each variant allele in a pair of case and control samples. For detection of somatic mutations, the case and control samples can be the tumor and normal sample from the same individual.
	"""
	
	cran = "falcon" 

	version("0.2", md5="e43f44ee09343a4d2e2a9f858233fba8")

	depends_on("r@3.0.1:", type=("build", "run"))
