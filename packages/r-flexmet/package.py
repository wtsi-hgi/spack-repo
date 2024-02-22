# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlexmet(RPackage):
	"""Flexible Latent Trait Metrics using the Filtered Monotonic
Polynomial Item Response Model

	Application of the filtered monotonic polynomial (FMP) item response
    model to flexibly fit item response models. The package includes tools that
    allow the item response model to be build on any monotonic transformation of
    the latent trait metric, as described by Feuerstahler (2019) <doi:10.1007/s11336-018-9642-9>.
	"""
	
	cran = "flexmet" 

	version("1.1", md5="8f7ab117563d583afe09a3bd148f683d")

