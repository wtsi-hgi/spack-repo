# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSizepower(RPackage):
	"""Sample Size and Power Calculation in Micorarray Studies

	This package has been prepared to assist users in computing either a sample size or power value for a microarray experimental study. The user is referred to the cited references for technical background on the methodology underpinning these calculations. This package provides support for five types of sample size and power calculations. These five types can be adapted in various ways to encompass many of the standard designs encountered in practice.
	"""
	
	bioc = "sizepower" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/sizepower_1.72.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/sizepower/sizepower_1.72.0.tar.gz"]

	version("1.72.0", sha256="fd3581187bce67e1318864b5b0db3e2cc2030fb6cad66246d4b93f325997840f")

