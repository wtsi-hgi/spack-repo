# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComics(RPackage):
	"""Computational Methods for Immune Cell-Type Subsets

	Provided are Computational methods for Immune Cell-type Subsets, including:(1) DCQ (Digital Cell Quantifier) to infer global dynamic changes in immune cell quantities within a complex tissue; and (2) VoCAL (Variation of Cell-type Abundance Loci) a deconvolution-based method that utilizes transcriptome data to infer the quantities of immune-cell types, and then uses these quantitative traits to uncover the underlying DNA loci.
	"""
	
	homepage = "http://dcq.tau.ac.il/"
	cran = "ComICS" 

	version("1.0.4", md5="7dedea1e70bade0cf4a3f236f38182f3")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
