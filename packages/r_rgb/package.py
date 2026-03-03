# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgb(RPackage):
	"""The R Genome Browser

	Classes and methods to efficiently handle (slice, annotate, draw ...) genomic features (such as genes or transcripts), and an interactive interface to browse them. Performances and main features are highlighted in Mareschal et al (2014) <doi:10.1093/bioinformatics/btu185>.
	"""
	
	homepage = "https://bioinformatics.ovsa.fr/Rgb"
	cran = "Rgb" 

	version("1.7.5", md5="ea150ee7223bfcd7b8699ac39cae2f89")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("tcl@8.6:", type=("build", "link", "run"))
	depends_on("tk@8.6:", type=("build", "link", "run"))
