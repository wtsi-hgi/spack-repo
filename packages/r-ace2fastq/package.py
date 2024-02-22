# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAce2fastq(RPackage):
	"""ACE File to FASTQ Converter

	The ACE file format is used in genomics to store contigs from sequencing machines.
  This tools converts it into FASTQ format. Both formats contain the 
  sequence characters and their
  corresponding quality information. Unlike the FASTQ file, the ace file stores the
  quality values numerically.
  The conversion algorithm uses the standard Sanger formula. The package facilitates insertion
  into pipelines, and content inspection.
	"""
	
	homepage = "https://github.com/c5sire/ace2fastq"
	cran = "ace2fastq" 

	version("0.6.0", md5="06ca563cb9583866ac55273138a359a8")

	depends_on("r-stringr", type=("build", "run"))
