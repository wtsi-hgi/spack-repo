# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHapmap100kxba(RPackage):
	"""Sample data - Hapmap 100K XBA Affymetrix

	Sample dataset obtained from http://www.hapmap.org
	"""
	
	bioc = "hapmap100kxba" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/hapmap100kxba_1.44.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/hapmap100kxba/hapmap100kxba_1.44.0.tar.gz"]

	version("1.44.0", md5="b4a619fb108a36920109307fbf63985b")


	# experiment