# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScent(RPackage):
	"""Single Cell Entropy Analysis of Gene Heterogeneity in Cell
Populations

	Analyse single cell RNA sequencing data using entropy to
    calculate heterogeneity and homogeneity of genes amongst the cell
    population. From the work of Michael J. Casey, Ruben J. Sanchez-Garcia 
    and Ben D. MacArthur.
	"""
	
	cran = "SCEnt" 

	version("0.0.1", md5="8ba062dfc6e3c311469259570b4949a1")

	depends_on("r-entropy", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
