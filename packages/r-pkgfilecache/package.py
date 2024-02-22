# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPkgfilecache(RPackage):
	"""Download and Manage Optional Package Data

	Manage optional data for your package. The data can be hosted anywhere, and you have to give a Uniform Resource Locator (URL) for each file. File integrity checks are supported. This is useful for package authors who need to ship more than the 5 Megabyte of data currently allowed by the the Comprehensive R Archive Network (CRAN).
	"""
	
	homepage = "https://github.com/dfsp-spirit/pkgfilecache"
	cran = "pkgfilecache" 

	version("0.1.5", md5="8f850f9396b0ac9d98f9fe20dec77cc3")

	depends_on("r-downloader", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
