# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAmigaffh(RPackage):
	"""Commodore Amiga File Format Handler

	Modern software often poorly support older file formats. This
    package intends to handle many file formats that were native to the
    antiquated Commodore Amiga machine. This package focuses on file types from
    the older Amiga operating systems (<= 3.0). It will read and write specific
    file formats and coerces them into more contemporary data.
	"""
	
	cran = "AmigaFFH" 

	version("0.4.3", md5="2cdfae768625544358967d5cad727119")

	depends_on("r-tuner@1:", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
