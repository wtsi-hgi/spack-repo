# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRelatable(RPackage):
	"""Functions for Mapping Key-Value Pairs, Many-to-Many,
One-to-Many, and Many-to-One Relations

	Functions to safely map from a vector of keys to a vector of values, determine properties of a given relation, or ensure a relation conforms to a given type, such as many-to-many, one-to-many, injective, surjective, or bijective. Permits default return values for use similar to a vectorised switch statement, as well as safely handling large vectors, NAs, and duplicate mappings.
	"""
	
	homepage = "https://github.com/domjarkey/relatable"
	cran = "relatable" 

	version("1.0.0", md5="ccc9ace7af9df1d37fa7ccfedb2746f2")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-compare@0.2.6:", type=("build", "run"))
