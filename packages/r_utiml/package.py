# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUtiml(RPackage):
	"""Utilities for Multi-Label Learning

	Multi-label learning strategies and others procedures to support multi-
  label classification in R. The package provides a set of multi-label procedures such as
  sampling methods, transformation strategies, threshold functions, pre-processing 
  techniques and evaluation metrics. A complete overview of the matter can be seen in
  Zhang, M. and Zhou, Z. (2014) <doi:10.1109/TKDE.2013.39> and Gibaja, E. and 
  Ventura, S. (2015) A Tutorial on Multi-label Learning.
	"""
	
	homepage = "https://github.com/rivolli/utiml"
	cran = "utiml" 

	version("0.1.7", md5="136ff017ca95d4e95e4e4867560dd588")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mldr@0.4:", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
