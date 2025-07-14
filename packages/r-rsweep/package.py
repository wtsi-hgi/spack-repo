# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsweep(RPackage):
	"""Functions to creation of low dimensional comparative matrices of Amino Acid Sequence occurrences

	The SWeeP method was developed to favor the analizes between amino acids sequences and to assist alignment free phylogenetic studies. This method is based on the concept of sparse words, which is applied in the scan of biological sequences and its the conversion in a matrix of ocurrences. Aiming the generation of low dimensional matrices of Amino Acid Sequence occurrences.
	"""
	
	bioc = "rSWeeP" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/rSWeeP_1.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/rSWeeP/rSWeeP_1.14.0.tar.gz"]

    version("1.20.0", tag="RELEASE_3_21")
	version("1.14.0", sha256="35fe330ae5c234368d290d23ac82d8aeca91c104e479ce4ab3acb4f3842c3664")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
