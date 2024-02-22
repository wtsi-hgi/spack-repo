# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFroth(RPackage):
	"""Emulate a 'Forth' Programming Environment

	Emulates a 'Forth' programming environment with added features to interface between R and 'Forth'. Implements most of the functionality described in the original "Starting Forth" textbook <https://www.forth.com/starting-forth/>.
	"""
	
	homepage = "https://www.ahl27.com/froth/"
	cran = "froth" 

	version("1.0.0", md5="77354875ad027c36e09e85270c693649")

	depends_on("r@4.3:", type=("build", "run"))
