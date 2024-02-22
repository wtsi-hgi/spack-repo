# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRconfig(RPackage):
	"""Manage R Configuration at the Command Line

	Configuration management using files (YAML, JSON, INI, TXT),
  JSON strings, and command line arguments. Command line arguments
  can be used to override configuration. Period-separated command line
  flags are parsed as hierarchical lists. Environment variables, R global variables,
  and configuration values can be substituted.
	"""
	
	homepage = "https://github.com/analythium/rconfig"
	cran = "rconfig" 

	version("0.3.0", md5="e5b8621bce4e546fb843025b79f31725")

	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
