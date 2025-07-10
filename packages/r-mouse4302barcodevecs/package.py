# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMouse4302barcodevecs(RPackage):
	"""mouse4302 data for barcode

	Data used by the barcode package for microarrays of type mouse4302.
	"""
	
	bioc = "mouse4302barcodevecs" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/mouse4302barcodevecs_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/mouse4302barcodevecs/mouse4302barcodevecs_1.40.0.tar.gz"]

	version("1.40.0", sha256="264f1e7b8a41debe52049d160a3f24456d2487321981f6f2a447f8ae71a74bd0")

	depends_on("r@2.10:", type=("build", "run"))

