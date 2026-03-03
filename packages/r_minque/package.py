# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMinque(RPackage):
	"""Various Linear Mixed Model Analyses

	This package offers three important components: (1) to construct a use-defined linear mixed model, (2) to employ one of linear mixed model approaches: minimum norm quadratic unbiased estimation (MINQUE) (Rao, 1971) for variance component estimation and random effect prediction; and (3) to employ a jackknife resampling technique to conduct various statistical tests. In addition, this package provides the function for model or data evaluations.This R package offers fast computations for large data sets analyses for various irregular data structures.
	"""
	
	cran = "minque" 

	version("2.0.0", md5="63f874f5aa9cdbd56c840f1259e49bbe")

