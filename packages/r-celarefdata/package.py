# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCelarefdata(RPackage):
	"""Processed scRNA data for celaref Vignette - cell labelling by reference

	This experiment data contains some processed data used in the celaref package vignette. These are publically available datasets, that have been processed by celaref package, and can be manipulated further with it.
	"""
	
	bioc = "celarefData"

	version("1.26.0", commit="f6ab93a6e99c635fc02701f0d88c0f107bb92bee")
	version("1.20.0", commit="e61d116a47baf4ea2c18f7f852dd4280b263b20a")

	depends_on("r@3.5:", type=("build", "run"))

