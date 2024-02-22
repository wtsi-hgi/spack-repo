# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDgca(RPackage):
	"""Differential Gene Correlation Analysis

	Performs differential correlation analysis on input
    matrices, with multiple conditions specified by a design matrix. Contains
    functions to filter, process, save, visualize, and interpret differential
    correlations of identifier-pairs across the entire identifier space, or with
    respect to a particular set of identifiers (e.g., one). Also contains several
    functions to perform differential correlation analysis on clusters (i.e., modules)
    or genes. Finally, it contains functions to generate empirical p-values for the
    hypothesis tests and adjust them for multiple comparisons. Although the package
    was built with gene expression data in mind, it is applicable to other types of
    genomics data as well, in addition to being potentially applicable to data from
    other fields entirely. It is described more fully in the manuscript
    introducing it, freely available at <doi:10.1186/s12918-016-0349-1>.
	"""
	
	cran = "DGCA" 

	version("1.0.3", md5="afe50740875b0e574727c356899a936a")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-wgcna", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
