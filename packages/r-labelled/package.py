# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLabelled(RPackage):
	"""Manipulating Labelled Data.

	Work with labelled data imported from 'SPSS' or 'Stata' with 'haven' or
	'foreign'. This package provides useful functions to deal with
	"haven_labelled" and "haven_labelled_spss" classes introduced by 'haven'
	package."""

	cran = "labelled"

	license("GPL-3.0-or-later")

	version("2.12.0", md5="401ed8a893355755d5bdbbaa5b294dd0")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-haven@2.4.1:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
