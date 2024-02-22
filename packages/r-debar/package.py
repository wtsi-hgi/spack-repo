# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDebar(RPackage):
	"""A Post-Clustering Denoiser for COI-5P Barcode Data

	The 'debar' sequence processing pipeline is designed for denoising high throughput 
    sequencing data for the animal DNA barcode marker cytochrome c oxidase I (COI). The package 
    is designed to detect and correct insertion and deletion errors within sequencer outputs. 
    This is accomplished through comparison of input sequences against a profile hidden Markov 
    model (PHMM) using the Viterbi algorithm (for algorithm details see Durbin et al. 1998, 
    ISBN: 9780521629713). Inserted base pairs are removed and deleted base pairs are accounted 
    for through the introduction of a placeholder character. Since the PHMM is a probabilistic 
    representation of the COI barcode, corrections are not always perfect. For this reason 
    'debar' censors base pairs adjacent to reported indel sites, turning them into placeholder 
    characters (default is 7 base pairs in either direction, this feature can be disabled).
    Testing has shown that this censorship results in the correct sequence length being restored, 
    and erroneous base pairs being masked the vast majority of the time (>95%). 
	"""
	
	cran = "debar" 

	version("0.1.1", md5="3be52659ec76e1031ce906a522401244")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-aphid", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
