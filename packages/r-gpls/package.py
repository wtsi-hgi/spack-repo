# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGpls(RPackage):
	"""Classification using generalized partial least squares

	Classification using generalized partial least squares for two-group and multi-group (more than 2 group) classification.
	"""
	
	bioc = "gpls" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/gpls_1.74.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/gpls/gpls_1.74.0.tar.gz"]

	version("1.74.0", md5="db6bc720156a5f7571a34e64b1189d3b")

