# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGroan(RPackage):
	"""Genomic Regression Workbench

	Workbench for testing genomic regression accuracy on
    (optionally noisy) phenotypes.
	"""
	
	cran = "GROAN" 

	version("1.3.1", md5="59cf8f3d9096d85bdfaba1580ee227c5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rrblup", type=("build", "run"))
