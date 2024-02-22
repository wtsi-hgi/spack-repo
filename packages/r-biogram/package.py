# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiogram(RPackage):
	"""N-Gram Analysis of Biological Sequences

	Tools for extraction and analysis of various
    n-grams (k-mers) derived from biological sequences (proteins
    or nucleic acids). Contains QuiPT (quick permutation test) for fast
    feature-filtering of the n-gram data.
	"""
	
	homepage = "https://github.com/michbur/biogram"
	cran = "biogram" 

	version("1.6.3", md5="52c249a7b38ff792e645c823c9b8774f")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-entropy", type=("build", "run"))
	depends_on("r-partitions", type=("build", "run"))
