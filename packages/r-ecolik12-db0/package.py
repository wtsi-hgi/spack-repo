# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcolik12Db0(RPackage):
	"""Base Level Annotation databases for E coli K12 Strain

	Base annotation databases for E coli K12 Strain, intended ONLY to be used by AnnotationDbi to produce regular annotation packages.
	"""
	
	bioc = "ecoliK12.db0" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/ecoliK12.db0_3.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/ecoliK12.db0/ecoliK12.db0_3.18.0.tar.gz"]

	version("3.18.0", sha256="f6d2d879eeefdcf57fe0f9a3c457835ad3170e4fcf299973fcbbdb2243bc12f4", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/ecoliK12.db0_3.18.0.tar.gz")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi@1.63.2:", type=("build", "run"))

