# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhitestr(RPackage):
	"""Analyzing the Heterogeneity of Single-Cell Populations

	A bioinformatics method developed for analyzing the heterogeneity of single-cell populations. Phitest provides an objective and automatic method to evaluate the performance of clustering and quality of cell clusters.
	"""
	
	cran = "PhitestR" 

	version("0.2.0", md5="a2360906a50d024ff3f52ecdb5740d0e")

	depends_on("r-fitdistrplus", type=("build", "run"))
