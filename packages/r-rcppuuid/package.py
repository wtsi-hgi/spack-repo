# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppuuid(RPackage):
	"""Generating Universally Unique Identificators

	Provides functions to generating a vector of Universally Unique Identifiers (UUID).
  Used implementation from the Boost C++ library. Supported random (version 4) and name (version 5)
  UUIDs.
	"""
	
	homepage = "https://artemklevtsov.gitlab.io/rcppuuid"
	cran = "RcppUUID" 

	version("1.1.1", md5="b032e17d8f562cb79b3cbdde5c3a97a5")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
