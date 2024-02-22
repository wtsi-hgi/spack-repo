# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRca(RPackage):
	"""Relational Class Analysis

	Relational Class Analysis (RCA) is a method for detecting
        heterogeneity in attitudinal data (as described in Goldberg
        A., 2011, Am. J. Soc, 116(5)).
	"""
	
	cran = "RCA" 

	version("2.0", md5="ec9f87683fb413b339c2271bd0f86bf0")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
