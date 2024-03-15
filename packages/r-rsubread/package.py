# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsubread(RPackage):
	"""Mapping, quantification and variant analysis of sequencing data"""

	bioc = "Rsubread"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Rsubread_2.16.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Rsubread/Rsubread_2.16.1.tar.gz"]

	version("2.16.1", md5="ec5687eb02901ff3b62915cf37aa48b4")

	depends_on("r-matrix", type=("build", "run"))
