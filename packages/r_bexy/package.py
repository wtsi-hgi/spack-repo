# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBexy(RPackage):
	"""Visualize and Parse the Output of 'BeXY'

	Provides functions for summarizing and plotting the output of the command-line tool 'BeXY' (<https://bitbucket.org/wegmannlab/bexy>), a tool that performs Bayesian inference of sex chromosome karyotypes and sex-linked scaffolds from low-depth sequencing data.
	"""
	
	cran = "bexy" 

	version("0.1.2", md5="d2f192a274346d2a7c9a732cdb5c94a6")

	depends_on("r-teachingdemos", type=("build", "run"))
	depends_on("r-ternary", type=("build", "run"))
