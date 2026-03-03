# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSchorsch(RPackage):
	"""Tools for Analyzing Factorial Experiments

	Offers a helping hand to psychologists and other behavioral scientists who routinely deal with experimental data from factorial experiments. It includes several functions to format output from other R functions according to the style guidelines of the APA (American Psychological Association). This formatted output can be copied directly into manuscripts to facilitate data reporting. These features are backed up by a toolkit of several small helper functions, e.g., offering out-of-the-box outlier removal. The package lends its name to Georg "Schorsch" Schuessler, ingenious technician at the Department of Psychology III, University of Wuerzburg. For details on the implemented methods, see Roland Pfister and Markus Janczyk (2016) <doi: 10.20982/tqmp.12.2.p147>.
	"""
	
	homepage = "https://www.tqmp.org/RegularArticles/vol12-2/p147/index.html"
	cran = "schoRsch" 

	version("1.10", md5="f4c125c764cb060522f1f419c1832223")

