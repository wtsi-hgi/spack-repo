# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBethel(RPackage):
	"""Bethel's algorithm

	The sample size according to the Bethel's procedure.
	"""
	
	cran = "bethel" 

	version("0.2", md5="8db0996514e4ece141ceda229fdcc180")

	depends_on("r@2.5:", type=("build", "run"))
