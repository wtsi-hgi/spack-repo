# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSynapterdata(RPackage):
	"""Data accompanying the synapter package

	Data independant acquisition of UPS1 protein mix in an E. coli background obtained on a Waters Synapt G2 instrument.
	"""
	
	bioc = "synapterdata"

	version("1.46.0", commit="cff53dbe27247cbaa00d0b5323800f1b3c60628d")
	version("1.40.0", commit="6e59823d965f520b7a1dca597aa517182bbbbc18")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-synapter@1.99.2:", type=("build", "run"))

