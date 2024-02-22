# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeneplastDataStringV91(RPackage):
	"""Input data for the geneplast package

	The package geneplast.data.string.v91 contains input data used in the analysis pipelines available in the geneplast package.
	"""
	
	bioc = "geneplast.data.string.v91" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/geneplast.data.string.v91_0.99.6.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/geneplast.data.string.v91/geneplast.data.string.v91_0.99.6.tar.gz"]

	version("0.99.6", md5="86433f8489d9228c5ed73e2b75a55398", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/geneplast.data.string.v91_0.99.6.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))

	# annotation