# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLfactors(RPackage):
	"""Factors with Levels

	Provides an extension to factors called 'lfactor' that are similar
    to factors but allows users to refer to 'lfactor' levels by either the level or
    the label.
	"""
	
	cran = "lfactors" 

	version("1.0.4", md5="d40aa46bf23340998fdb63b10f921989")

	depends_on("r@3.1:", type=("build", "run"))
