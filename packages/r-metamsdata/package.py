# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetamsdata(RPackage):
	"""Example CDF data for the metaMS package

	Example CDF data for the metaMS package
	"""
	
	bioc = "metaMSdata" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/metaMSdata_1.38.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/metaMSdata/metaMSdata_1.38.0.tar.gz"]

	version("1.38.0", md5="aa7ca09c8f43104cb85f69fda0a1fc1a")


	# experiment