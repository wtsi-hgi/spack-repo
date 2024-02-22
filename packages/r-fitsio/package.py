# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFitsio(RPackage):
	"""FITS (Flexible Image Transport System) Utilities

	Utilities to read and write files in the FITS (Flexible
  Image Transport System) format, a standard format in astronomy (see
  e.g. <https://en.wikipedia.org/wiki/FITS> for more information).
  Present low-level routines allow: reading, parsing, and modifying
  FITS headers; reading FITS images (multi-dimensional arrays);
  reading FITS binary and ASCII tables; and writing FITS images
  (multi-dimensional arrays).  Higher-level functions allow: reading
  files composed of one or more headers and a single (perhaps
  multidimensional) image or single table; reading tables into
  data frames; generating vectors for image array axes; scaling and
  writing images as 16-bit integers.  Known incompletenesses are
  reading random group extensions, as well as
  complex and array descriptor data types in binary tables.
	"""
	
	cran = "FITSio" 

	version("2.1-6", md5="be8104864b836edfe9bbf1043059fdd4")

	depends_on("r@3:", type=("build", "run"))
