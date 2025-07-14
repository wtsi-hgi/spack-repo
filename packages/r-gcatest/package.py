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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/gcatest_2.2.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/gcatest/gcatest_2.2.0.tar.gz"]

    version("2.8.0", tag="RELEASE_3_21")
	version("2.2.0", sha256="7bbe749ec6948355ccfadc31ba00c8c42a037c18ed67d25ca95319249dc1cf42")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-lfa", type=("build", "run"))
