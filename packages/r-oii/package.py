# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROii(RPackage):
	"""Crosstab and Statistical Tests for OII MSc Stats Course

	Provides simple crosstab output with optional statistics (e.g., Goodman-Kruskal Gamma, Somers' d, and Kendall's tau-b) as well as two-way and one-way tables. The package is used within the statistics component of the Masters of Science (MSc) in Social Science of the Internet at the Oxford Internet Institute (OII), University of Oxford, but the functions should be useful for general data analysis and especially for analysis of categorical and ordinal data.
	"""
	
	cran = "oii" 

	version("1.0.2.1", md5="fca6eb63f8af9efcc001f01a5cad8a1e")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-rapportools", type=("build", "run"))
	depends_on("r-gmodels", type=("build", "run"))
	depends_on("r-deducer", type=("build", "run"))
