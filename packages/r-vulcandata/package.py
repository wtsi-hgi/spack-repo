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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/vulcandata_1.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/vulcandata/vulcandata_1.24.0.tar.gz"]

	version("1.30.0", tag="RELEASE_3_21")
	version("1.24.0", sha256="99b2f09af6adc8f1d99a68400ab377e298554837a99947ec6a55af7339ef8ba3")


