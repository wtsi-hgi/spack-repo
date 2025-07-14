# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu133plus2barcodevecs(RPackage):
	"""hgu133plus2 data for barcode

	Data used by the barcode package for microarrays of type hgu133plus2.
	"""
	
	bioc = "hgu133plus2barcodevecs" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/hgu133plus2barcodevecs_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/hgu133plus2barcodevecs/hgu133plus2barcodevecs_1.40.0.tar.gz"]

	version("1.46.0", tag="RELEASE_3_21")
	version("1.40.0", sha256="6ea1bfc84d5a0a6bb2131de9ec9e88c5a0ffe348041e3dcc908b58249a1864b0")

	depends_on("r@2.10:", type=("build", "run"))

