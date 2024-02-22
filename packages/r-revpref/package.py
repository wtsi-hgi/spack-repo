# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRevpref(RPackage):
	"""Tools for Computational Revealed Preference Analysis

	Tools to (i) check consistency of a finite set of consumer demand observations with a number of revealed preference axioms at a given efficiency level, (ii) compute goodness-of-fit indices when the data do not obey the axioms, and (iii) compute power against uniformly random behavior.
	"""
	
	homepage = "https://github.com/ksurana21/revpref"
	cran = "revpref" 

	version("0.1.0", md5="c9c809251f4aef8f11f2c6b15e829cda")

	depends_on("r-gtools", type=("build", "run"))
