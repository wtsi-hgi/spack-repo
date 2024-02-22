# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRandpack(RPackage):
	"""Randomization routines for Clinical Trials

	A suite of classes and functions for randomizing patients in clinical trials.
	"""
	
	bioc = "randPack" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/randPack_1.48.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/randPack/randPack_1.48.0.tar.gz"]

	version("1.48.0", md5="71791ade28f58d981a510c8b660ae1e7")

	depends_on("r-biobase", type=("build", "run"))
