# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFalconx(RPackage):
	"""Finding Allele-Specific Copy Number in Whole-Exome Sequencing
Data

	This is a method for Allele-specific DNA Copy Number profiling for whole-Exome sequencing data.  Given the allele-specific coverage and site biases at the variant loci, this program segments the genome into regions of homogeneous allele-specific copy number.  It requires, as input, the read counts for each variant allele in a pair of case and control samples, as well as the site biases. For detection of somatic mutations, the case and control samples can be the tumor and normal sample from the same individual.  The implemented method is based on the paper: Chen, H., Jiang, Y., Maxwell, K., Nathanson, K. and Zhang, N. (under review). Allele-specific copy number estimation by whole Exome sequencing.
	"""
	
	cran = "falconx" 

	version("0.2", md5="358b7fed7748468eb5664d4856540d52")

	depends_on("r@3.0.1:", type=("build", "run"))
