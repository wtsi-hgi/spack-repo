# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGencountr(RPackage):
	"""Interacting with Roberts and Utych's (2019) Gendered Language
Dictionary

	Allows users to generate a gendered language score according to the gendered language dictionary in Roberts and Utych (2019) <doi:10.1177/1065912919874883>.
	"""
	
	homepage = "https://gencounter.app.damoncroberts.com"
	cran = "genCountR" 

	version("1.0.0", md5="166d4b91de801b6b3b19d5c9731dacdc")

	depends_on("r@2.10:", type=("build", "run"))
