# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTciapathfinder(RPackage):
	"""Client for the Cancer Imaging Archive REST API

	A wrapper for The Cancer Imaging Archive's REST API. The Cancer
    Imaging Archive (TCIA) hosts de-identified medical images of cancer
    available for public download, as well as rich metadata for each image
    series. TCIA provides a REST API for programmatic access to the data.
    This package provides simple functions to access each API endpoint.
    For more information, see <https://github.com/pamelarussell/TCIApathfinder>
    and TCIA's website.
	"""
	
	cran = "TCIApathfinder" 

	version("1.0.6", md5="04b04e5ecdea414a6b636093308ac4b1")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
