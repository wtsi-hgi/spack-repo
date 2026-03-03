# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScontomatch(RPackage):
	"""Aligning Ontology Annotation Across Single Cell Datasets with
'scOntoMatch'

	Unequal granularity of cell type annotation makes it difficult to compare scRNA-seq datasets at scale. Leveraging the ontology system for defining cell type hierarchy, 'scOntoMatch' aims to align cell type annotations to make them comparable across studies. The alignment involves two core steps: first is to trim the cell type tree within each dataset so each cell type does not have descendants, and then map cell type labels cross-studies by direct matching and mapping descendants to ancestors. Various functions for plotting cell type trees and manipulating ontology terms are also provided. In the Single Cell Expression Atlas hosted at EBI, a compendium of datasets with curated ontology labels are great inputs to this package.
	"""
	
	homepage = "https://github.com/Papatheodorou-Group/scOntoMatch"
	cran = "scOntoMatch" 

	version("0.1.1", md5="d583009435a431e24badad6dc713a07a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ontologyindex", type=("build", "run"))
	depends_on("r-ontologyplot", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
