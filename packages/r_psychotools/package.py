# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsychotools(RPackage):
	"""Psychometric Modeling Infrastructure

	Infrastructure for psychometric modeling such as data classes (for
  item response data and paired comparisons), basic model fitting functions (for
  Bradley-Terry, Rasch, parametric logistic IRT, generalized partial credit,
  rating scale, multinomial processing tree models), extractor functions for
  different types of parameters (item, person, threshold, discrimination,
  guessing, upper asymptotes), unified inference and visualizations, and various
  datasets for illustration.  Intended as a common lightweight and efficient
  toolbox for psychometric modeling and a common building block for fitting
  psychometric mixture models in package "psychomix" and trees based on
  psychometric models in package "psychotree".
	"""
	
	cran = "psychotools" 

	version("0.7-3", md5="a8316dc55cbfe1784417d64cb1e7ae46")

	depends_on("r@3.6:", type=("build", "run"))
