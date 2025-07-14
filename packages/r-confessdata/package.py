# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConfessdata(RPackage):
	"""Example dataset for CONFESS package

	Example text-converted C01 image files for use in the CONFESS Bioconductor package.
	"""
	
	bioc = "CONFESSdata"

	version("1.36.0", commit="6ed905452661bc6a09498655a5e208407f4ef795")
	version("1.30.0", commit="52a202d7cdfdfb5408cfd5d9aafd8df8cadcc8b8")

	depends_on("r@3.3:", type=("build", "run"))

