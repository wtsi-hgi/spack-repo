# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnvir(RPackage):
	"""Manage R Environments Better

	Provides a small set of functions for managing R environments, with defaults designed to encourage usage patterns that scale well to larger code bases. It provides: import_from(), a flexible way to assign bindings that defaults to the current environment; include(), a vectorized alternative to base::source() that also default to the current environment; and attach_eval() and attach_source(), a way to evaluate expressions in attached environments. Together, these (and other) functions pair to provide a robust alternative to base::library() and base::source().
	"""
	
	homepage = "https://t-kalinowski.github.io/envir/"
	cran = "envir" 

	version("0.2.2", md5="2c7dd008215c6bcba9a2af5cc9a38f89")

