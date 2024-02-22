# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTabulog(RPackage):
	"""Parsing Semi-Structured Log Files into Tabular Format

	Convert semi-structured log files (such as 'Apache' access.log files)
    into a tabular format (data.frame) using a standard template system.
	"""
	
	cran = "tabulog" 

	version("0.1.1", md5="321cc201b126c4a117e8fc75e8691910")

	depends_on("r-yaml", type=("build", "run"))
