# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmpp(RPackage):
	"""Various Similarity and Distance Metrics for Marked Point
Processes

	Compute similarities and distances between marked point processes.
	"""
	
	cran = "mmpp" 

	version("0.6", md5="783e6c481ae9061c53c904b9c0434df5")

