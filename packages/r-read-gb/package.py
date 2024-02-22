# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReadGb(RPackage):
	"""Open GenBank Files

	Opens complete record(s) with .gb extension from the NCBI/GenBank Nucleotide database and returns a list containing shaped record(s). These kind of files contains detailed records of DNA samples (locus, organism, type of sequence, source of the sequence...). An example of record can be found at <https://www.ncbi.nlm.nih.gov/nuccore/HE799070>.
	"""
	
	cran = "read.gb" 

	version("2.2", md5="121e25524086903d9982a82751b98c69")

	depends_on("r-rentrez", type=("build", "run"))
