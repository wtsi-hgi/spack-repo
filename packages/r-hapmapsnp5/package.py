# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHapmapsnp5(RPackage):
	"""Sample data - Hapmap SNP 5.0 Affymetrix

	Sample dataset obtained from http://www.hapmap.org
	"""
	
	bioc = "hapmapsnp5" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/hapmapsnp5_1.44.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/hapmapsnp5/hapmapsnp5_1.44.0.tar.gz"]

	version("1.44.0", md5="2f14e60f39cf94c43f2dd0e5aa5a48e2", url="https://www.bioconductor.org/packages/release/data/experiment/src/contrib/hapmapsnp5_1.44.0.tar.gz")


	# experiment