# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhyext2(RPackage):
	"""An Extension (for Package 'SigTree') of Some of the Classes in
Package 'phylobase'

	Based on (but not identical to) the no-longer-maintained package 'phyext', provides enhancements to 'phylobase' classes, specifically for use by package 'SigTree'; provides classes and methods which help users manipulate branch-annotated trees (as in 'SigTree'); also provides support for a few other extra features.
	"""
	
	cran = "phyext2" 

	version("0.0.4", md5="fd259c1664803f52be3e353ba8cacb6c", url="https://cran.r-project.org/src/contrib/phyext2_0.0.4.tar.gz")

	depends_on("r-phylobase", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
