# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNoia(RPackage):
	"""Implementation of the Natural and Orthogonal InterAction (NOIA)
Model

	The NOIA model, as described extensively in Alvarez-Castro & Carlborg (2007), is a framework facilitating the estimation of genetic effects and genotype-to-phenotype maps. This package provides the basic tools to perform linear and multilinear regressions from real populations (provided the phenotype and the genotype of every individuals), estimating the genetic effects from different reference points, the genotypic values, and the decomposition of genetic variances in a multi-locus, 2 alleles system. This package is presented in Le Rouzic & Alvarez-Castro (2008). 
	"""
	
	homepage = "https://github.com/lerouzic/noia"
	cran = "noia" 

	version("0.97.3", md5="d0a2fd6b4d70c86c0785db52f339defc")

