# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKidpack(RPackage):
	"""DKFZ kidney package

	kidney microarray data
	"""
	
	homepage = "http://www.dkfz.de/mga"
	bioc = "kidpack"

	version("1.50.0", commit="ebde15c57ead87bab522f29478ea71bf7359e8a4")
	version("1.44.0", commit="3144e6cf67eb61358782428ecf2ccbd89490d06f")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))

