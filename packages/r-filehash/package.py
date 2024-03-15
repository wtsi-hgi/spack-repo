# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFilehash(RPackage):
	"""Simple Key-Value Database.

	Implements a simple key-value style database where character string keys
	are associated with data values that are stored on the disk. A simple
	interface is provided for inserting, retrieving, and deleting data from the
	database. Utilities are provided that allow 'filehash' databases to be
	treated much like environments and lists are already used in R. These
	utilities are provided to encourage interactive and exploratory analysis on
	large datasets. Three different file formats for representing the database
	are currently available and new formats can easily be incorporated by third
	parties for use in the 'filehash' framework."""

	cran = "filehash"

	license("GPL-2.0-or-later")

	version("2.4-5", md5="10fd32df52956b2bf7104f779024812d")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
