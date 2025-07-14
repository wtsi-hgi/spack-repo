# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu133abarcodevecs(RPackage):
	"""hgu133a data for barcode

	Data used by the barcode package for microarrays of type hgu133a.
	"""
	
	bioc = "hgu133abarcodevecs" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/hgu133abarcodevecs_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/hgu133abarcodevecs/hgu133abarcodevecs_1.40.0.tar.gz"]

	version("1.46.0", tag="RELEASE_3_21")
	version("1.40.0", sha256="5fd8767bd227560cac963896286ada6b49cef2bc89670139e7418da67ed51aed")

	depends_on("r@2.10:", type=("build", "run"))

