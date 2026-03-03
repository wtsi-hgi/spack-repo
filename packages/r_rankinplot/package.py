# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRankinplot(RPackage):
	"""Convenient Plotting for the Modified Rankin Scale and Other
Ordinal Outcome Data

	Provides convenient tools for visualising ordinal outcome data following the "Grotta Bar" approach pioneered by The National Institute of Neurological Disorders and Stroke rt-PA Stroke Study Group (1995) <doi:10.1056/NEJM199512143332401>.
	"""
	
	cran = "rankinPlot" 

	version("1.1.0", md5="5f0bc04dd90ba3386fb67abd419aaa85")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-scales@1.2:", type=("build", "run"))
