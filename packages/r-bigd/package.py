# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBigd(RPackage):
	"""Flexibly Format Dates and Times to a Given Locale

	Format dates and times flexibly and to whichever locales
    make sense. Parses dates, times, and date-times in various formats
    (including string-based ISO 8601 constructions). The formatting syntax gives
    the user many options for formatting the date and time output in a precise
    manner. Time zones in the input can be expressed in multiple ways and there
    are many options for formatting time zones in the output as well. Several of
    the provided helper functions allow for automatic generation of locale-aware
    formatting patterns based on date/time skeleton formats and standardized
    date/time formats with varying specificity.
	"""
	
	homepage = "https://github.com/rich-iannone/bigD"
	cran = "bigD" 

	version("0.2.0", md5="51f023fe40d1aabc705eec86d42c73f5")

	depends_on("r@3.2:", type=("build", "run"))
