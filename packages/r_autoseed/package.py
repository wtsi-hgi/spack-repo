# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAutoseed(RPackage):
	"""Retrieve Disease-Related Genes from Public Sources

	For researchers to quickly and comprehensively acquire disease genes, so as to understand the mechanism of disease,
  we developed this program to acquire disease-related genes.
  The data is integrated from three public databases. The three databases are 'eDGAR', 'DrugBank'
  and 'MalaCards'. The 'eDGAR' is a comprehensive database, containing data on the relationship between disease and genes.
  'DrugBank' contains information on 13443 drugs and 5157 targets. 'MalaCards' integrates human disease information, including disease-related genes.
	"""
	
	cran = "Autoseed" 

	version("0.1.0", md5="6274b568c1b54e6bd78c0014a06dd5ba")

	depends_on("r@3.5:", type=("build", "run"))
