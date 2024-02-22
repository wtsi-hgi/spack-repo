# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlier(RPackage):
	"""Implements the Affymetrix PLIER algorithm

	The PLIER (Probe Logarithmic Error Intensity Estimate) method produces an improved signal by accounting for experimentally observed patterns in probe behavior and handling error at the appropriately at low and high signal values.
	"""
	
	bioc = "plier" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/plier_1.72.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/plier/plier_1.72.0.tar.gz"]

	version("1.72.0", md5="f16a09bf8bccc7f5596d55ed0577a593")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
