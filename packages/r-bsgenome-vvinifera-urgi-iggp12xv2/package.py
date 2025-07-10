# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeVviniferaUrgiIggp12xv2(RPackage):
	"""Full reference nuclear genome sequences for Vitis vinifera subsp. vinifera PN40024 (IGGP version 12Xv2)

	Full reference nuclear genome sequences for Vitis vinifera subsp. vinifera PN40024 (derived from Pinot Noir and close to homozygosity after 6-9 rounds of selfing) as assembled by the IGGP (version 12Xv2) and available at the URGI (INRA)
	"""
	
	bioc = "BSgenome.Vvinifera.URGI.IGGP12Xv2" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Vvinifera.URGI.IGGP12Xv2_0.1.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Vvinifera.URGI.IGGP12Xv2/BSgenome.Vvinifera.URGI.IGGP12Xv2_0.1.tar.gz"]

	version("0.1", sha256="32e8ed009b81ab1349c69511ad41413b3baf6f59785408af1c83bf72a2de4ae9", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Vvinifera.URGI.IGGP12Xv2_0.1.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

