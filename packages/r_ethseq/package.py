# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REthseq(RPackage):
	"""Ethnicity Annotation from Whole-Exome and Targeted Sequencing
Data

	Reliable and rapid ethnicity annotation from whole exome and targeted sequencing data.
	"""
	
	cran = "EthSEQ" 

	version("3.0.2", md5="1e7a3ac6f408617e15af2461291f3742")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-mass@7.3.47:", type=("build", "run"))
	depends_on("r-geometry@0.3.6:", type=("build", "run"))
	depends_on("r-data-table@1.10:", type=("build", "run"))
	depends_on("r-snprelate@1.8:", type=("build", "run"))
	depends_on("r-gdsfmt@1.10.1:", type=("build", "run"))
	depends_on("r-plot3d@1.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
