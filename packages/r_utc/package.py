# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUtc(RPackage):
	"""Coordinated Universal Time Transformations

	Three functions are provided: first function changes time from local to UTC, other changes from UTC to local and third returns difference between local and UTC. %h+% operator is also provided it adds hours to a time.
	"""
	
	cran = "utc" 

	version("0.1.5", md5="13a532d808283bc93e9dd6b909ee1921")

