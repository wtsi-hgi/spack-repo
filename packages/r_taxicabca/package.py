# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTaxicabca(RPackage):
	"""Taxicab Correspondence Analysis

	Computation and visualization of Taxicab Correspondence Analysis, Choulakian (2006) <doi:10.1007/s11336-004-1231-4>.  Classical correspondence analysis (CA) is a statistical method to analyse 2-dimensional tables of positive numbers and is typically applied to contingency tables (Benzecri, J.-P. (1973). L'Analyse des Donnees. Volume II. L'Analyse des Correspondances. Paris, France: Dunod).  Classical CA is based on the Euclidean distance.  Taxicab CA is like classical CA but is based on the Taxicab or Manhattan distance.  For some tables, Taxicab CA gives more informative results than classical CA.
	"""
	
	cran = "TaxicabCA" 

	version("0.1.1", md5="c7ddf6a8b67cb67f146d70d616f5396c")

