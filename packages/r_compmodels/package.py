# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCompmodels(RPackage):
	"""Pseudo Computer Models for Optimization

	A suite of computer model test functions that can be used to test and evaluate algorithms for Bayesian (also known as sequential) optimization. Some of the functions have known functional forms, however, most are intended to serve as black-box functions where evaluation requires running computer code that reveals little about the functional forms of the objective and/or constraints. The primary goal of the package is to provide users (especially those who do not have access to real computer models) a source of reproducible and shareable examples that can be used for benchmarking algorithms. The package is a living repository, and so more functions will be added over time. For function suggestions, please do contact the author of the package.
	"""
	
	cran = "CompModels" 

	version("0.3.0", md5="7c5021fbcc8a1c7c457bb728fda57a78")

