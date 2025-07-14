# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGdsarray(RPackage):
	"""Representing GDS files as array-like objects

	GDS files are widely used to represent genotyping or sequence data. The GDSArray package implements the `GDSArray` class to represent nodes in GDS files in a matrix-like representation that allows easy manipulation (e.g., subsetting, mathematical transformation) in _R_. The data remains on disk until needed, so that very large files can be processed.
	"""
	
	homepage = "https://github.com/Bioconductor/GDSArray"
	bioc = "GDSArray"

	version("1.28.0", commit="62b4f52fb1c2e2eef203a895b13d4679266eaf79")
	version("1.22.0", commit="5357cff43cfdbde1cbd28add8e0e5b981a823a57")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gdsfmt", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-delayedarray@0.5.32:", type=("build", "run"))
	depends_on("r-s4vectors@0.17.34:", type=("build", "run"))
	depends_on("r-snprelate", type=("build", "run"))
	depends_on("r-seqarray", type=("build", "run"))
