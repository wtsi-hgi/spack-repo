# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCountland(RPackage):
	"""Analysis of Biological Count Data, Especially from Single-Cell
RNA-Seq

	A set of functions for applying a 
    restricted linear algebra to the analysis of 
    count-based data. See the accompanying preprint
    manuscript: "Normalizing need not be the norm:
    count-based math for analyzing single-cell data"
    Church et al (2022) <doi:10.1101/2022.06.01.494334>
    This tool is specifically designed to analyze 
    count matrices from single cell RNA sequencing 
    assays. The tools implement several count-based
    approaches for standard steps in single-cell 
    RNA-seq analysis, including scoring genes and cells, 
    comparing cells and clustering, calculating differential 
    gene expression, and several methods for rank 
    reduction. There are many opportunities for further
    optimization that may prove useful in the analysis of
    other data. We provide the source code freely
    available at <https://github.com/shchurch/countland>
    and encourage users and developers to fork the code for 
    their own purposes. 
	"""
	
	homepage = "https://github.com/shchurch/countland"
	cran = "countland" 

	version("0.1.2", md5="476e3f8b49e1155414a26eca3fb4076e")

	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
