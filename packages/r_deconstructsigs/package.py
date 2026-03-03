# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeconstructsigs(RPackage):
	"""Identifies Signatures Present in a Tumor Sample

	Takes sample information in the form of the fraction of mutations
    in each of 96 trinucleotide contexts and identifies the weighted combination
    of published signatures that, when summed, most closely reconstructs the
    mutational profile.
	"""
	
	homepage = "https://github.com/raerose01/deconstructSigs"
	cran = "deconstructSigs" 

	version("1.8.0", md5="007bc39e38cb2e9b2ed634b4f6fe2f96")

	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-bsgenome-hsapiens-ucsc-hg19", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
