# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForeign(RPackage):
	"""Read Data Stored by 'Minitab', 'S', 'SAS', 'SPSS', 'Stata', 'Systat',
	'Weka', 'dBase', ...

	Reading and writing data stored by some versions of 'Epi Info', 'Minitab',
	'S', 'SAS', 'SPSS', 'Stata', 'Systat', 'Weka', and for reading and writing
	some 'dBase' files."""

	cran = "foreign"

	license("GPL-2.0-or-later")

	version("0.8-86", md5="96b42e5a8b7344b99e19b9be63a73d23")

	depends_on("r@4:", type=("build", "run"))
