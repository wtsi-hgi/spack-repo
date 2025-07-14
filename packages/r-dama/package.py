# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDama(RPackage):
	"""Efficient design and analysis of factorial two-colour microarray data

	This package contains functions for the efficient design of factorial two-colour microarray experiments and for the statistical analysis of factorial microarray data. Statistical details are described in Bretz et al. (2003, submitted)
	"""
	
	homepage = "http://www.microarrays.med.uni-goettingen.de"
	bioc = "daMA" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/daMA_1.74.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/daMA/daMA_1.74.0.tar.gz"]

	version("1.80.0", tag="RELEASE_3_21")
	version("1.74.0", sha256="668c9830927a9bb44df8f84565e9731ae6bc77aa9e04b80cee8afaa60c4473b2")

	depends_on("r-mass", type=("build", "run"))
