# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RColonca(RPackage):
	"""exprSet for Alon et al. (1999) colon cancer data

	exprSet for Alon et al. (1999) colon cancer data
	"""
	
	bioc = "colonCA" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/colonCA_1.44.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/colonCA/colonCA_1.44.0.tar.gz"]

	version("1.44.0", md5="d12f03a7ded676f392dbbb26bbbef174")

	depends_on("r-biobase@2.5.5:", type=("build", "run"))

