# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPbs(RPackage):
	"""Periodic B Splines

	Periodic B Splines Basis
	"""
	
	cran = "pbs" 

	version("1.1", md5="7cd8047c922f00a97f124b0527490a3c")

