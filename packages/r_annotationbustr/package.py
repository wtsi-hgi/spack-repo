# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnnotationbustr(RPackage):
	"""Extract Subsequences from GenBank Annotations

	Extraction of subsequences into FASTA files from GenBank annotations where gene names may vary among accessions. Borstein & O'Meara (2018) <doi:10.7717/peerj.5179>.
	"""
	
	homepage = "https://github.com/sborstein/AnnotationBustR"
	cran = "AnnotationBustR" 

	version("1.3.0", md5="12f26973d561c52554803f477cc2b52e")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ape@4.1:", type=("build", "run"))
	depends_on("r-seqinr@3.3.6:", type=("build", "run"))
