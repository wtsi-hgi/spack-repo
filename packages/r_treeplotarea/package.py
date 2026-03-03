# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreeplotarea(RPackage):
	"""Correction Factors for Tree Plot Areas Intersected by Stand
Boundaries

	The German national forest inventory uses angle count sampling, 
    a sampling method first published as `Bitterlich, W.: Die Winkelzählmessung.
    Allgemeine Forst- und Holzwirtschaftliche Zeitung, 58. Jahrg., Folge 11/12 
    vom Juni 1947` and extended by Grosenbaugh
    (<https://academic.oup.com/jof/article-abstract/50/1/32/4684174>)
    as probability proportional to size sampling.
    When plots are located near stand boundaries, their sizes and hence
    their probabilities need to be corrected.
	"""
	
	homepage = "https://gitlab.com/fvafrcu/treeplotarea.git"
	cran = "treePlotArea" 

	version("2.0.0", md5="83e5f45132793751d1648c294ef11fba")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-fritools", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
