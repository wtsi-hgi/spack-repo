# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJot(RPackage):
	"""Jot Down Values for Later

	Reproducible work requires a record of where every statistic originated.
    When writing reports, some data is too big to load in the same environment and some statistics take a while to compute.
    This package offers a way to keep notes on statistics, simple functions, and small objects.
    Notepads can be locked to avoid accidental updates.
    Notepads keep track of who added the notes and when the notes were added.
    A simple text representation is used to allow for clear version histories.
	"""
	
	homepage = "http://christophertkenny.com/jot/"
	cran = "jot" 

	version("0.0.4", md5="4c2b17054758e1a6d6145b05f5da4a4a")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
