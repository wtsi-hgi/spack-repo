# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFritools2(RPackage):
	"""Utilities for the Forest Research Institute of the State
Baden-Wuerttemberg

	Miscellaneous utilities, tools and helper
    functions for finding and searching files on disk, searching for and
    removing R objects from the workspace.
    Does not import or depend on any third party package, but on core R 
    only (i.e. it may depend on packages with priority 'base').
	"""
	
	homepage = "https://gitlab.com/fvafrcu/fritools"
	cran = "fritools2" 

	version("4.1.0", md5="1fc2704a49f7fa771dc5d8ad8495411a", url="https://cran.r-project.org/src/contrib/fritools2_4.1.0.tar.gz")

	depends_on("r@3.3:", type=("build", "run"))
