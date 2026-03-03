# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFolders(RPackage):
	"""Standardized Folder Names

	Supports the use of standardized folder names.
	"""
	
	homepage = "https://github.com/deohs/folders"
	cran = "folders" 

	version("0.1.0", md5="63c6dd0200f49f8ef0c39719798ddcd9")
	version("0.0.8", md5="73e9c921e4e908d08c30258f65bd3869")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-config@0.3:", type=("build", "run"))
	depends_on("r-here@0.1:", type=("build", "run"))
	depends_on("r-yaml@2.2.1:", type=("build", "run"))
