# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGcatest(RPackage):
	"""Genotype Conditional Association TEST

	GCAT is an association test for genome wide association studies that controls for population structure under a general class of trait models.  This test conditions on the trait, which makes it immune to confounding by unmodeled environmental factors.  Population structure is modeled via logistic factors, which are estimated using the `lfa` package.
	"""
	
	homepage = "https://github.com/StoreyLab/gcatest"
	bioc = "gcatest"

	version("2.8.0", commit="4861b9e6f6e8c549e32179b381c1619eb8dcf451")
	version("2.2.0", commit="f3875f759286fefeadaf30531806e7b52482b151")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-lfa", type=("build", "run"))
