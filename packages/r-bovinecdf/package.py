# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBovinecdf(RPackage):
	"""bovinecdf

	A package containing an environment representing the Bovine.cdf file.
	"""
	
	bioc = "bovinecdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/bovinecdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/bovinecdf/bovinecdf_2.18.0.tar.gz"]

	version("2.18.0", md5="e155fc7d5f84ee420d9b250a639af305")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation