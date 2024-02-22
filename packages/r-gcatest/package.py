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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/gcatest_2.2.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/gcatest/gcatest_2.2.0.tar.gz"]

	version("2.2.0", md5="ddfda402a2332e9c16ecfaa035b689a9")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-lfa", type=("build", "run"))
