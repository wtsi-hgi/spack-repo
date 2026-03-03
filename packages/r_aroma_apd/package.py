# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAromaApd(RPackage):
	"""A Probe-Level Data File Format Used by 'aroma.affymetrix'
[deprecated]

	DEPRECATED. Do not start building new projects based on this package. (The (in-house) APD file format was initially developed to store Affymetrix probe-level data, e.g. normalized CEL intensities.  Chip types can be added to APD file and similar to methods in the affxparser package, this package provides methods to read APDs organized by units (probesets).  In addition, the probe elements can be arranged optimally such that the elements are guaranteed to be read in order when, for instance, data is read unit by unit.  This speeds up the read substantially.  This package is supporting the Aroma framework and should not be used elsewhere.)
	"""
	
	homepage = "URL:"
	cran = "aroma.apd" 

	version("0.7.0", md5="8378b2a1880dc55fdc8047b63705da05")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-r-methodss3@1.7.1:", type=("build", "run"))
	depends_on("r-r-oo@1.23:", type=("build", "run"))
	depends_on("r-r-utils@2.2:", type=("build", "run"))
	depends_on("r-r-huge@0.9:", type=("build", "run"))
