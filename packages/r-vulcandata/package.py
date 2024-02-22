# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVulcandata(RPackage):
	"""VirtUaL ChIP-Seq data Analysis using Networks, dummy dataset

	This package provides a dummy regulatory network and ChIP-Seq dataset for running examples in the vulcan package
	"""
	
	bioc = "vulcandata" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/vulcandata_1.24.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/vulcandata/vulcandata_1.24.0.tar.gz"]

	version("1.24.0", md5="cd95ea7ac7f2b9edfd46c1ffccb7c3c1")


	# experiment