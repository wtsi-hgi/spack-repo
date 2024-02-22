# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCinid(RPackage):
	"""Curculionidae INstar IDentification

	Method for identifying the instar of Curculionid larvae from the observed distribution of the headcapsule size of mature larvae.
	"""
	
	cran = "CINID" 

	version("1.3-0", md5="842f057033152207894d41773f207dc1")

