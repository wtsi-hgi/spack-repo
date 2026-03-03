# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPkgnews(RPackage):
	"""Retrieve R Package News Files

	Read R package news files, regardless of whether or not the package
  is installed.
	"""
	
	homepage = "https://github.com/owenjonesuob/pkgnews"
	cran = "pkgnews" 

	version("0.0.2", md5="9238bde0df86b3b362404c4d6bf2026f")

	depends_on("pandoc", type=("build", "link", "run"))
