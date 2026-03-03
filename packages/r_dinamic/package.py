# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDinamic(RPackage):
	"""A Method to Analyze Recurrent DNA Copy Number Aberrations in
Tumors

	In tumor tissue, underlying genomic instability can lead to DNA copy number alterations,
	e.g., copy number gains or losses. Sporadic copy number alterations occur randomly throughout the
	genome, whereas recurrent alterations are observed in the same genomic region across multiple
	independent samples, perhaps because they provide a selective growth advantage.
	This package implements the DiNAMIC procedure for assessing the statistical significance of 
	recurrent DNA copy number aberrations (Bioinformatics (2011) 27(5) 678 - 685).
	"""
	
	cran = "dinamic" 

	version("1.0.1", md5="6d4e005b3c4349b6ae6e41675e149a4d")
	version("1.0", md5="f77353caed46518fd6e1f325145eabf1")

	depends_on("r@4.2:", type=("build", "run"))
