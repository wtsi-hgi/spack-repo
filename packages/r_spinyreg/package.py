# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpinyreg(RPackage):
	"""Sparse Generative Model and Its EM Algorithm

	Implements a generative model that uses a
    spike-and-slab like prior distribution obtained by multiplying a
    deterministic binary vector. Such a model allows an EM algorithm,
    optimizing a type-II log-likelihood.
	"""
	
	cran = "spinyReg" 

	version("0.1-0", md5="23248c2adf6604e27da44ccd6b5ef4ba")

