# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoenocliner(RPackage):
	"""Coenocline Simulation

	Simulate species occurrence and abundances (counts) along
    gradients.
	"""
	
	homepage = "https://github.com/gavinsimpson/coenocliner/"
	cran = "coenocliner" 

	version("0.2-3", md5="e410f8f1f03511d55ab070cceb77d978")

