# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProzor(RPackage):
	"""Minimal Protein Set Explaining Peptide Spectrum Matches

	Determine minimal protein set explaining
    peptide spectrum matches. Utility functions for creating fasta amino acid databases with decoys and contaminants.
    Peptide false discovery rate estimation for target decoy search results on psm, precursor, peptide and protein
    level. Computing dynamic swath window sizes based on MS1 or MS2 signal distributions.
	"""
	
	homepage = "https://github.com/protviz/prozor"
	cran = "prozor" 

	version("0.3.1", md5="e812018c19ea91a5d467eef166f1fa81")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ahocorasicktrie", type=("build", "run"))
	depends_on("r-docopt", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
