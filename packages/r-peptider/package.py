# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPeptider(RPackage):
	"""Evaluation of Diversity in Nucleotide Libraries

	Evaluation of diversity in peptide libraries, including NNN, NNB,
    NNK/S, and 20/20 schemes. Custom encoding schemes can also be defined.
    Metrics for evaluation include expected coverage, relative efficiency, and
    the functional diversity of the library. Peptide-level inclusion
    probabilities are computable for both the native and custom encoding
    schemes.
	"""
	
	homepage = "https://github.com/heike/peptider"
	cran = "peptider" 

	version("0.2.2", md5="e2def15e5c169af616978ff3145a31fc")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-discreterv@1.2:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
