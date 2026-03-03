# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHetu(RPackage):
	"""Structural Handling of Finnish Personal Identity Codes

	Structural handling of Finnish identity codes (natural persons and 
    organizations); extract information, check ID validity and diagnostics.
	"""
	
	homepage = "https://ropengov.github.io/hetu/"
	cran = "hetu" 

	version("1.0.7", md5="ac757a56508e814e9a35b09aa44b8e70")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
