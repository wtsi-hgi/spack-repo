# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProcess(RPackage):
	"""Ciphergen SELDI-TOF Processing

	A package for processing protein mass spectrometry data.
	"""
	
	bioc = "PROcess" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/PROcess_1.78.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/PROcess/PROcess_1.78.0.tar.gz"]

    version("1.84.0", tag="RELEASE_3_21")
	version("1.78.0", sha256="f2ee603d4d072a2fab0fac819981a00f3dbcb2751813e264fd8f738bcb9f9043")

	depends_on("r-icens", type=("build", "run"))
