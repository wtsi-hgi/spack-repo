# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRlog(RPackage):
	"""A Simple, Opinionated Logging Utility

	A very lightweight package that writes out log messages in an opinionated way.
  Simpler and lighter than other logging packages, 'rlog' provides a compact feature set that
  focuses on getting the job done in a Unix-like way.
	"""
	
	homepage = "https://github.com/sellorm/rlog"
	cran = "rlog" 

	version("0.1.0", md5="edde36f92ce406257080e0bc2c876fff")

