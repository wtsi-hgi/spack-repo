# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProvtracer(RPackage):
	"""Uses Provenance to Trace File Lineage for One or more R Scripts

	Uses provenance collected by 'rdtLite' package or comparable tool
    to display information about input files, output files, and exchanged files
    for a single R script or a series of R scripts.
	"""
	
	homepage = "https://github.com/End-to-end-provenance"
	cran = "provTraceR" 

	version("1.0", md5="41170c2260392d8364e67d143b5927c7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-provparser@0.3:", type=("build", "run"))
