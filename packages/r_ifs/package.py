# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIfs(RPackage):
	"""Iterated Function Systems

	Iterated Function Systems Estimator as in Iacus and La Torre (2005) <doi:10.1155/JAMDS.2005.33>.
	"""
	
	cran = "ifs" 

	version("0.1.10", md5="2ee347f5bb4b6215b999dc06340bc13c")

