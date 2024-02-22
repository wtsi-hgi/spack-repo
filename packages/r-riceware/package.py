# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRiceware(RPackage):
	"""A Diceware Passphrase Implementation

	The Diceware method can be used to generate strong passphrases.
  In short, you roll a 6-faced dice 5 times in a row, the number obtained is
  matched against a dictionary of easily remembered words. By combining together 7
  words thus generated, you obtain a password that is relatively easy to remember,
  but would take several millions years (on average) for a powerful computer to guess.
	"""
	
	homepage = "https://github.com/fmichonneau/riceware"
	cran = "riceware" 

	version("0.4", md5="ff346e155414a1bc0c74517e0ac000a6")

	depends_on("r@3.1.3:", type=("build", "run"))
	depends_on("r-random@0.2.4:", type=("build", "run"))
