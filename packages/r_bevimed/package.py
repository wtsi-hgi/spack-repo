# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBevimed(RPackage):
	"""Bayesian Evaluation of Variant Involvement in Mendelian Disease

	A fast integrative genetic association test for rare diseases based on a model for disease status given allele counts at rare variant sites. Probability of association, mode of inheritance and probability of pathogenicity for individual variants are all inferred in a Bayesian framework - 'A Fast Association Test for Identifying Pathogenic Variants Involved in Rare Diseases', Greene et al 2017 <doi:10.1016/j.ajhg.2017.05.015>.
	"""
	
	cran = "BeviMed" 

	version("5.8", md5="264703c402b37a77d5c8bfb3721b6898")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
