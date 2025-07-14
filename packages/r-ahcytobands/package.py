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
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/AHCytoBands_0.99.1.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/AHCytoBands/AHCytoBands_0.99.1.tar.gz"]

    version("0.99.1", tag="RELEASE_3_21")
	version("0.99.1", sha256="7bb5a06b5a8c0c2024f317ed0c58b048550ba9ed6cc64266c4afc03a24ec7d6b")

	depends_on("r@3.2.2:", type=("build", "run"))

