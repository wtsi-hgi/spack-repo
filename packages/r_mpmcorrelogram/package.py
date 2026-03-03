# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMpmcorrelogram(RPackage):
	"""Multivariate Partial Mantel Correlogram

	Functions to compute and plot multivariate (partial) Mantel correlograms.
	"""
	
	cran = "mpmcorrelogram" 

	version("0.1-4", md5="e3d96bfb609fe120ffabb94f468b7cee")

	depends_on("r-vegan", type=("build", "run"))
