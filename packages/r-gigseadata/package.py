# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGigseadata(RPackage):
	"""Gene set collections for the GIGSEA package

	The gene set collection used for the GIGSEA package.
	"""
	
	bioc = "GIGSEAdata"

	version("1.26.0", commit="4e9bfb3d6c83ab288bb2fc6620d198d9774bdcc0")
	version("1.20.0", commit="bd836c5f46115adc735686162b4cde785b1b8ad8")

	depends_on("r@3.5:", type=("build", "run"))

