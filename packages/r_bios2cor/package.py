# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBios2cor(RPackage):
	"""From Biological Sequences and Simulations to Correlation
Analysis

	Utilities for computation and analysis of correlation/covariation in multiple sequence alignments and in side chain motions during molecular dynamics simulations. Features include the computation of correlation/covariation scores using a variety of scoring functions between either sequence positions in alignments or side chain dihedral angles in molecular dynamics simulations and utilities to analyze the correlation/covariation matrix through a variety of tools including network representation and principal components analysis. In addition, several utility functions are based on the R graphical environment to provide friendly tools for help in data interpretation. Examples of sequence covariation analysis are provided in: (1) Pele J, Moreau M, Abdi H, Rodien P, Castel H, Chabbert M (2014) <doi:10.1002/prot.24570> and (2) Taddese B, Deniaud M, Garnier A, Tiss A, Guissouma H, Abdi H, Henrion D, Chabbert M (2018) <doi: 10.1371/journal.pcbi.1006209>. An example of side chain correlated motion analysis is provided in: Taddese B, Garnier A, Abdi H, Henrion D, Chabbert M (2020) <doi: 10.1038/s41598-020-72766-1>. This work was supported by the French National Research Agency (Grant number: ANR-11-BSV2-026) and by GENCI (Grant number: 100567).
	"""
	
	cran = "Bios2cor" 

	version("2.2.1", md5="4e2130721ade866bb01d5ea10e2c284c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bio3d", type=("build", "run"))
	depends_on("r-circular", type=("build", "run"))
	depends_on("r-bigmemory", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
