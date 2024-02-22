# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPvldcurve(RPackage):
	"""Simplifies the Analysis of Pressure Volume and Leaf Drying
Curves

	Simplifies the manufacturing, analysis and display of pressure volume and leaf drying curves. From the progression of the curves turgor loss point, osmotic potential, apoplastic fraction as well as minimum conductance and stomatal closure can be derived. Methods adapted from Bartlett, Scoffoni, Sack (2012) <doi:10.1111/j.1461-0248.2012.01751.x> and Sack, Scoffoni, PrometheusWikiContributors (2011) <http://prometheuswiki.org/tiki-index.php?page=Minimum+epidermal+conductance+%28gmin%2C+a.k.a.+cuticular+conductance%29>.
	"""
	
	cran = "pvldcurve" 

	version("1.2.6", md5="b0fecaf54e58ddfe48775619ef2b921b")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
