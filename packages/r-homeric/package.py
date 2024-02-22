# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHomeric(RPackage):
	"""Doughnut Plots

	A simple implementation of doughnut plots - pie charts with a blank center. The package is named after Homer Simpson - arguably the best-known lover of doughnuts.
	"""
	
	cran = "Homeric" 

	version("0.1-3", md5="094a2c86f77765f9cc20936251987218")

