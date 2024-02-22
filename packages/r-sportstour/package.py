# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSportstour(RPackage):
	"""Display Tournament Fixtures using Knock Out and Round Robin
Techniques

	Use of Knock Out and Round Robin Techniques in preparing tournament fixtures as discussed in the Book Health and Physical Education by 'Dr. V K Sharma'(2018,ISBN:978-93-5272-134-4).
	"""
	
	cran = "SportsTour" 

	version("0.1.0", md5="dc0e7d3127c591928c713838c8d1593f")

