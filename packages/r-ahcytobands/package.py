# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAhcytobands(RPackage):
	"""CytoBands for AnnotationHub

	Supplies AnnotationHub with CytoBand information from UCSC. There is a track for each major organism. Giemsa-stained bands are commonly used to decorate chromosomal overviews in visualizations of genomic data.
	"""
	
	bioc = "AHCytoBands"

	version("0.99.1", commit="821428ca2c99127167ddb9c733f571a5f21a1bf6")
	version("0.99.1", commit="821428ca2c99127167ddb9c733f571a5f21a1bf6")

	depends_on("r@3.2.2:", type=("build", "run"))

