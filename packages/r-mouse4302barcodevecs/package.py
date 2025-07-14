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

	version("1.46.0", commit="5371a746c6ce42b659b35ee382e5cfe9c1f12f5b")
	version("1.40.0", commit="f3973934570d818014c41af86f2a65a069901536")

	depends_on("r@2.10:", type=("build", "run"))

