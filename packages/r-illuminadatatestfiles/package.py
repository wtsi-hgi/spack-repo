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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/IlluminaDataTestFiles_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/IlluminaDataTestFiles/IlluminaDataTestFiles_1.40.0.tar.gz"]

    version("1.46.0", tag="RELEASE_3_21")
	version("1.40.0", sha256="d1eb2baa08b869a10056c5d1582063d03a2dc468cc9075332d6a4ac9bd3acb21")


