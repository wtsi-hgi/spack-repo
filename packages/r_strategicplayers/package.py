# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStrategicplayers(RPackage):
	"""Strategic Players

	Identifies individuals in a social network who should be the intervention
    subjects for a network intervention in which you have a group of targets, a
    group of avoiders, and a group that is neither.
	"""
	
	cran = "strategicplayers" 

	version("1.1", md5="b363ba650ea7900ec6ae176883facaff")

