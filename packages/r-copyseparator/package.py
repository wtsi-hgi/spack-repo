# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCopyseparator(RPackage):
	"""Assembling Long Gene Copies from Short Read Data

	Assembles two or more gene copies from short-read Next-Generation Sequencing data. Works best when there are only two gene copies and read length >=250 base pairs. High and relatively even coverage are important.
	"""
	
	homepage = "https://github.com/LeiYang-Fish/copyseparator"
	cran = "copyseparator" 

	version("1.2.0", md5="ddb82ec119839a42125a7bb2172fea9c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-kmer", type=("build", "run"))
	depends_on("r-decipher", type=("build", "run"))
	depends_on("r-beepr", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
