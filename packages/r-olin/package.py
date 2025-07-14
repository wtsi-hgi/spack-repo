# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROlin(RPackage):
	"""Optimized local intensity-dependent normalisation of two-color microarrays

	Functions for normalisation of two-color microarrays by optimised local regression and for detection of artefacts in microarray data
	"""
	
	homepage = "http://olin.sysbiolab.eu"
	bioc = "OLIN"

	version("1.86.0", commit="64088335029e5dbe805428e16eea0c65108904c6")
	version("1.80.0", commit="aafe32fc71050e2187a3e3919089a2e237edd3ba")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))
	depends_on("r-marray", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
