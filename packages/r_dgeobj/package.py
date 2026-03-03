# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDgeobj(RPackage):
	"""Differential Gene Expression (DGE) Analysis Results Data Object

	
    Provides a flexible container to manage and annotate Differential Gene 
    Expression (DGE) analysis results (Smythe et. al (2015) <doi:10.1093/nar/gkv007>).  
    The DGEobj has data slots for row (gene), col (samples), assays (matrix n-rows 
    by m-samples dimensions) and metadata (not keyed to row, col, or assays).  
    A set of accessory functions to deposit, query and retrieve subsets of a data 
    workflow has been provided.  Attributes are used to capture metadata such as 
    species and gene model, including reproducibility information such that a 3rd 
    party can access a DGEobj history to see how each data object was created or 
    modified.  Since the DGEobj is customizable and extensible it is not limited 
    to RNA-seq analysis types of workflows -- it can accommodate nearly any data 
    analysis workflow that starts from a matrix of assays (rows) by samples (columns).
	"""
	
	cran = "DGEobj" 

	version("1.1.2", md5="8d84369964ade6ee4707681568feb390")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
