# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnvdocument(RPackage):
	"""Document the R Working Environment

	Prints out information about the R working environment
    (system, R version,loaded and attached packages and versions) from a single
    function "env_doc()".  Optionally adds information on git repository,
    tags, commits and remotes (if available).
	"""
	
	homepage = "https://github.com/dgJacks0n/envDocument"
	cran = "envDocument" 

	version("2.4.1", md5="344d5760dcc650a5d6536fa3bdf9ba1c")

