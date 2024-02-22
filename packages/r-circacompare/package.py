# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCircacompare(RPackage):
	"""Analyses of Circadian Data

	Uses non-linear regression to statistically compare two circadian rhythms.
    Groups are only compared if both are rhythmic (amplitude is non-zero).
    Performs analyses regarding mesor, phase, and amplitude, reporting on estimates and statistical differences, for each, between groups.
    Details can be found in Parsons et al (2020) <doi:10.1093/bioinformatics/btz730>.
	"""
	
	homepage = "https://rwparsons.github.io/circacompare/"
	cran = "circacompare" 

	version("0.2.0", md5="1bfdda7fd4f1cd6ddd02263e081eef16")

	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
