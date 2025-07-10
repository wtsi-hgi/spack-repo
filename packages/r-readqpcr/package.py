# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReadqpcr(RPackage):
	"""Read qPCR data

	The package provides functions to read raw RT-qPCR data of different platforms.
	"""
	
	homepage = "http://www.bioconductor.org/packages/release/bioc/html/ReadqPCR.html"
	bioc = "ReadqPCR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ReadqPCR_1.48.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ReadqPCR/ReadqPCR_1.48.0.tar.gz"]

	version("1.48.0", sha256="23316bb543f9860adc987b207c41488a0a3b0bfd28c37681415ba5f3555186a7")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
