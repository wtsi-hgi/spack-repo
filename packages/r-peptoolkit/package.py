# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPeptoolkit(RPackage):
	"""A Toolkit for Using Peptide Sequences in Machine Learning

	This toolkit is designed for manipulation and analysis of peptides. It provides functionalities to assist researchers in peptide engineering and proteomics. Users can manipulate peptides by adding amino acids at every position, count occurrences of each amino acid at each position, and transform amino acid counts based on probabilities. The package offers functionalities to select the best versus the worst peptides and analyze these peptides, which includes counting specific residues, reducing peptide sequences, extracting features through One Hot Encoding (OHE), and utilizing Quantitative Structure-Activity Relationship (QSAR) properties (based in the package 'Peptides' by Osorio et al. (2015) <doi:10.32614/RJ-2015-001>). This package is intended for both researchers and bioinformatics enthusiasts working on peptide-based projects, especially for their use with machine learning.
	"""
	
	homepage = "https://github.com/jrcodina/peptoolkit"
	cran = "peptoolkit" 

	version("0.0.1", md5="d4fc5c8426e0a0c11d11d84909420a89")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-peptides", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
