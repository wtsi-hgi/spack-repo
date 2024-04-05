# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu95av2(RPackage):
	"""Affymetrix Human Genome U95 Set Annotation Data (hgu95av2)

	Affymetrix Human Genome U95 Set annotation data (hgu95av2) assembled using data from public data repositories
	"""
	
	bioc = "hgu95av2" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgu95av2_2.2.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgu95av2/hgu95av2_2.2.0.tar.gz"]

	version("2.2.0", md5="b92585c0f43e91bd1abd234b9465a6a7", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgu95av2_2.2.0.tar.gz")

	depends_on("r@2.4:", type=("build", "run"))

