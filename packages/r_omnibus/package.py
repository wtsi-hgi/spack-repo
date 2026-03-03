# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROmnibus(RPackage):
	"""Helper Tools for Managing Data, Dates, Missing Values, and Text

	An assortment of helper functions for managing data (e.g.,
	rotating values in matrices by a user-defined angle, switching from
	row- to column-indexing), dates (e.g., intuiting year from messy date
	strings), handling missing values (e.g., removing elements/rows across
	multiple vectors or matrices if any have an NA), text (e.g.,
	flushing reports to the console in real-time); and combining data frames
	with different schema (copying, filling, or concatenating columns or
	applying functions before combining).
	"""
	
	homepage = "https://github.com/adamlilith/omnibus"
	cran = "omnibus" 

	version("1.2.9", md5="f2897d36c7caa88b5940502f63dbc994")

	depends_on("r@3.5:", type=("build", "run"))
