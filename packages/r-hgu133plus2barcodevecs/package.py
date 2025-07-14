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

	version("1.46.0", commit="649f8f5595053064787cec032b940d0b0a40f1bd")
	version("1.40.0", commit="3182f63ad6a7b19a858d6f3198d63449d84b7bf5")

	depends_on("r@2.10:", type=("build", "run"))

