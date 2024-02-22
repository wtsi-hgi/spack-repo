# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMirnameconverter(RPackage):
	"""Convert miRNA Names to Different miRBase Versions

	Translating mature miRNA names to different miRBase versions, sequence retrieval, checking names for validity and detecting miRBase version of a given set of names (data from http://www.mirbase.org/).
	"""
	
	bioc = "miRNAmeConverter" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/miRNAmeConverter_1.30.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/miRNAmeConverter/miRNAmeConverter_1.30.0.tar.gz"]

	version("1.30.0", md5="cfc6563f669ecbc03292cccba919fe05")

	depends_on("r-mirbaseversions-db", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
