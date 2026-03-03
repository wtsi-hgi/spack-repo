# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatetimeoffset(RPackage):
	"""Datetimes with Optional UTC Offsets and/or Heterogeneous Time
Zones

	Supports import/export for a number of datetime string standards 
    and R datetime classes often including
    lossless re-export of     
    any original reduced precision including 'ISO 8601' <https://en.wikipedia.org/wiki/ISO_8601> and 
    'pdfmark' <https://opensource.adobe.com/dc-acrobat-sdk-docs/library/pdfmark/> datetime strings.
    Supports local/global datetimes with optional UTC offsets and/or (possibly heterogeneous) time zones
    with up to nanosecond precision.
	"""
	
	homepage = "https://trevorldavis.com/R/datetimeoffset/dev/"
	cran = "datetimeoffset" 

	version("0.3.1", md5="f43c562d3eb48860b189191c0eaa7f17")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-clock", type=("build", "run"))
	depends_on("r-purrr@1:", type=("build", "run"))
	depends_on("r-vctrs@0.5:", type=("build", "run"))
