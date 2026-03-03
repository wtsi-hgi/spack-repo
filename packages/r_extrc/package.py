# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExtrc(RPackage):
	"""Extended RC Models for Contingency Tables

	Maximum likelihood estimation of an extended class of row-column (RC) association models for two-dimensional contingency tables, which are formulated by a condition of reduced rank on a matrix of extended association parameters; see Forcina (2019) <arXiv:1910.13848>. These parameters are defined by choosing the logit type for the row and column variables among four different options and a transformation derived from suitable divergence measures.
	"""
	
	cran = "extRC" 

	version("1.2", md5="3f0877e2caae15a1a5531c7566946dbe")

	depends_on("r-mass", type=("build", "run"))
