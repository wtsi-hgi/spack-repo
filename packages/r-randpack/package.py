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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/randPack_1.48.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/randPack/randPack_1.48.0.tar.gz"]

    version("1.54.0", tag="RELEASE_3_21")
	version("1.48.0", sha256="d3610cdc9225f9fe70c93a75a08b6472f33ece9fcbe24fd1fb19d9222842c1e1")

	depends_on("r-biobase", type=("build", "run"))
