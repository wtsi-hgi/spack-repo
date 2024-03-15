# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCtc(RPackage):
	"""Cluster and Tree Conversion.

	Tools for export and import classification trees and clusters to other
	programs"""

	bioc = "ctc"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ctc_1.76.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ctc/ctc_1.76.0.tar.gz"]

	version("1.76.0", md5="ea94b8b636b26d4f827ecd4569804d1e")

	depends_on("r-amap", type=("build", "run"))
