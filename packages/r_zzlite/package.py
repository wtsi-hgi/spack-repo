# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZzlite(RPackage):
	"""Lite Wrapper for the 'Zamzar File Conversion' API

	A minor collection of HTTP wrappers for the 'Zamzar File Conversion'
    API. The wrappers makes it easy to utilize the API and thus convert
    between more than 100 different file formats (ranging from audio files,
    images, movie formats, etc., etc.) through an R session.  
    For specifics regarding the API, please see <https://developers.zamzar.com/>.
	"""
	
	cran = "zzlite" 

	version("0.1.2", md5="2698c39a6f1c7e634db063345746e5f8")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
