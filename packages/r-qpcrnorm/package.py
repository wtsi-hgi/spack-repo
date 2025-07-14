# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQpcrnorm(RPackage):
	"""Data-driven normalization strategies for high-throughput qPCR data.

	The package contains functions to perform normalization of high-throughput qPCR data. Basic functions for processing raw Ct data plus functions to generate diagnostic plots are also available.
	"""
	
	bioc = "qpcrNorm"

	version("1.66.0", commit="a5fa0f41035c4532e0fe64895861c8c50f1fe1fb")
	version("1.60.0", commit="93f193125a68cec3d06e464d229e4b0311a9c85d")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
