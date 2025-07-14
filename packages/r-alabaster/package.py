# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlabaster(RPackage):
	"""Umbrella for the Alabaster Framework

	Umbrella for the alabaster suite, providing a single-line import for all alabaster.* packages. Installing this package ensures that all known alabaster.* packages are also installed, avoiding problems with missing packages when a staging method or loading function is dynamically requested. Obviously, this comes at the cost of needing to install more packages, so advanced users and application developers may prefer to install the required alabaster.* packages individually.
	"""
	
	bioc = "alabaster" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/alabaster_1.2.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/alabaster/alabaster_1.2.0.tar.gz"]

	version("1.8.0", tag="RELEASE_3_21")
	version("1.2.0", sha256="6d08f588c49200b514395245055d4628fabdd044aceabff0b4dd6b2e0b858050")

	depends_on("r-alabaster-base", type=("build", "run"))
	depends_on("r-alabaster-matrix", type=("build", "run"))
	depends_on("r-alabaster-ranges", type=("build", "run"))
	depends_on("r-alabaster-se", type=("build", "run"))
	depends_on("r-alabaster-sce", type=("build", "run"))
	depends_on("r-alabaster-spatial", type=("build", "run"))
	depends_on("r-alabaster-string", type=("build", "run"))
	depends_on("r-alabaster-vcf", type=("build", "run"))
	depends_on("r-alabaster-bumpy", type=("build", "run"))
	depends_on("r-alabaster-mae", type=("build", "run"))
