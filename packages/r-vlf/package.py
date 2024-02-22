# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVlf(RPackage):
	"""Frequency Matrix Approach for Assessing Very Low Frequency
Variants in Sequence Records

	Using frequency matrices, very low frequency variants (VLFs) are assessed for amino acid and nucleotide sequences.  The VLFs are then compared to see if they occur in only one member of a species, singleton VLFs, or if they occur in multiple members of a species, shared VLFs.  The amino acid and nucleotide VLFs are then compared to see if they are concordant with one another.  Amino acid VLFs are also assessed to determine if they lead to a change in amino acid residue type, and potential changes to protein structures. Based on Stoeckle and Kerr (2012) <doi:10.1371/journal.pone.0043992>.
	"""
	
	cran = "VLF" 

	version("1.1", md5="b8d521eb7910186fd6d8eead49f2e813")

	depends_on("r@2.10:", type=("build", "run"))
