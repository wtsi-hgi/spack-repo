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

	version("1.78.0", md5="9a9b6e6d31c1c45fb08e1f7cf00f0170")

	depends_on("r-icens", type=("build", "run"))
