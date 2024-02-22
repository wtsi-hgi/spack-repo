# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIlluminadatatestfiles(RPackage):
	"""Illumina microarray files (IDAT) for testing

	Example data for Illumina microarray output files, for testing purposes
	"""
	
	bioc = "IlluminaDataTestFiles" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/IlluminaDataTestFiles_1.40.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/IlluminaDataTestFiles/IlluminaDataTestFiles_1.40.0.tar.gz"]

	version("1.40.0", md5="3afa4b143fbb1dd18b3a7acd8f2984b1")


	# experiment