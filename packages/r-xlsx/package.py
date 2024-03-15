# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXlsx(RPackage):
	"""Read, Write, Format Excel 2007 and Excel 97/2000/XP/2003 Files.

	Provide R functions to read/write/format Excel 2007 and Excel
	97/2000/XP/2003 file formats."""

	cran = "xlsx"

	license("GPL-3.0-only")

	version("0.6.5", md5="838e6843c8e958afced89b64c1c563f3")

	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-xlsxjars", type=("build", "run"))
	depends_on("openjdk@1.6:", type=("build", "link", "run"))
