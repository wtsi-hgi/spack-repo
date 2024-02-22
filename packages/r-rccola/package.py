# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRccola(RPackage):
	"""Safely Manage API Keys and Load Data from a REDCap or Other
Source

	The handling of an API key (misnomer for password) for protected
    data can be difficult. This package provides secure convenience functions for 
    entering / handling API keys and pulling data directly into memory. By default
    it will load from REDCap instances, but other sources are injectable via
    inversion of control.
	"""
	
	homepage = "https://github.com/spgarbet/rccola"
	cran = "rccola" 

	version("1.0.2", md5="2280ab675124b4a70c2d3f3a940ea71b")

	depends_on("r-redcapapi", type=("build", "run"))
	depends_on("r-getpass", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-keyring@1.3:", type=("build", "run"))
