# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeoscale(RPackage):
	"""Geological Time Scale Plotting

	Functionality for adding the geological timescale to bivariate plots.
	"""
	
	cran = "geoscale" 

	version("2.0.1", md5="fb8f89a553c5f4495ccccf243ae10e14")

	depends_on("r@2.10:", type=("build", "run"))
