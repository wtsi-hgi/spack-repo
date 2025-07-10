# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLydata(RPackage):
	"""Example Dataset for crossmeta Package

	Raw data downloaded from GEO for the compound LY294002. Raw data is from multiple platforms from Affymetrix and Illumina. This data is used to illustrate the cross-platform meta-analysis of microarray data using the crossmeta package.
	"""
	
	bioc = "lydata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/lydata_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/lydata/lydata_1.28.0.tar.gz"]

	version("1.28.0", sha256="19475d674a72fa35c4fabbc5d524add1a6f90db4b87a3846e96e066c028e8a3f")


