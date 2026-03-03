# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXr(RPackage):
	"""A Structure for Interfaces from R

	Support for interfaces from R to other languages,
    built around a class for evaluators and a combination of functions, classes and
    methods for communication. Will be used through a specific language interface
    package. Described in the book "Extending R".
	"""
	
	cran = "XR" 

	version("0.7.2", md5="f3e8b2bc8ab0bab3a6d66b478ca1d19a")

	depends_on("r-jsonlite", type=("build", "run"))
