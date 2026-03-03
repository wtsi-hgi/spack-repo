# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProjecttemplate(RPackage):
	"""Automates the Creation of New Statistical Analysis Projects

	Provides functions to
    automatically build a directory structure for a new R
    project. Using this structure, 'ProjectTemplate'
    automates data loading, preprocessing, library
    importing and unit testing.
	"""
	
	homepage = "http://projecttemplate.net"
	cran = "ProjectTemplate" 

	version("0.10.4", md5="caa41113dfdd73c46edd9febff553b64")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
