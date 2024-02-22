# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAsrgenomics(RPackage):
	"""Complementary Genomic Functions

	Presents a series of molecular and genetic routines in the R
    environment with the aim of assisting in analytical pipelines before
    and after the use of 'asreml' or another library to perform analyses such
    as Genomic Selection or Genome-Wide Association Analyses. 
    Methods and examples are described in Gezan, Oliveira, Galli, and Murray (2022) 
    <https://asreml.kb.vsni.co.uk/wp-content/uploads/sites/3/ASRgenomics_Manual.pdf>.
	"""
	
	cran = "ASRgenomics" 

	version("1.1.4", md5="451ab3c3d99a74c784b345bc8c9b0a73")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-aghmatrix", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
	depends_on("r-factoextra", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-scattermore", type=("build", "run"))
	depends_on("r-superheat", type=("build", "run"))
