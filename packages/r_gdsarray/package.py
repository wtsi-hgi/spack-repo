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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GDSArray_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GDSArray/GDSArray_1.22.0.tar.gz"]

	version("1.22.0", md5="3ae99d95017d67dd67e17f47436f0301")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gdsfmt", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-delayedarray@0.5.32:", type=("build", "run"))
	depends_on("r-s4vectors@0.17.34:", type=("build", "run"))
	depends_on("r-snprelate", type=("build", "run"))
	depends_on("r-seqarray", type=("build", "run"))
