# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWebsearchr(RPackage):
	"""Access Domains and Search Popular Websites

	Functions that allow for accessing domains and a number of search engines.
	"""
	
	homepage = "https://github.com/fschaff/websearchr"
	cran = "websearchr" 

	version("0.0.3", md5="e274dbcd4c2f1db169842b2bd5202dba")

	depends_on("r@3.4:", type=("build", "run"))
