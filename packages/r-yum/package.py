# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYum(RPackage):
	"""Utilities to Extract and Process 'YAML' Fragments

	Provides a number of functions to facilitate
  extracting information in 'YAML' fragments from one or 
  multiple files, optionally structuring the information
  in a 'data.tree'. 'YAML' (recursive acronym for "YAML ain't
  Markup Language") is a convention for specifying structured
  data in a format that is both machine- and human-readable.
  'YAML' therefore lends itself well for embedding (meta)data
  in plain text files, such as Markdown files. This principle
  is implemented in 'yum' with minimal dependencies (i.e. only
  the 'yaml' packages, and the 'data.tree' package can be
  used to enable additional functionality).
	"""
	
	homepage = "https://r-packages.gitlab.io/yum"
	cran = "yum" 

	version("0.1.0", md5="a9e5b91b6b62de4bee3fb6cf7e19c4c3")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-yaml@2.2:", type=("build", "run"))
