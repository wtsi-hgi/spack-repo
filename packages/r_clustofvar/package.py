# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClustofvar(RPackage):
	"""Clustering of Variables

	Cluster analysis of a set of variables. Variables can be quantitative, qualitative or a mixture of both.
	"""
	
	cran = "ClustOfVar" 

	version("1.1", md5="cc747a93ed5e23d32930c0276196ef72")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-pcamixdata", type=("build", "run"))
