# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAhcytobands(RPackage):
	"""CytoBands for AnnotationHub

	Supplies AnnotationHub with CytoBand information from UCSC. There is a track for each major organism. Giemsa-stained bands are commonly used to decorate chromosomal overviews in visualizations of genomic data.
	"""
	
	bioc = "AHCytoBands" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/AHCytoBands_0.99.1.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/AHCytoBands/AHCytoBands_0.99.1.tar.gz"]

	version("0.99.1", md5="3dd85d02e7ed3fca4c7898b5e395edeb")

	depends_on("r@3.2.2:", type=("build", "run"))

	# annotation