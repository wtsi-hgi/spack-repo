# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REgseadata(RPackage):
	"""Gene set collections for the EGSEA package

	This package includes gene set collections that are used for the Ensemble of Gene Set Enrichment Analyses (EGSEA) method for gene set testing. It includes Human and Mouse versions of the MSidDB (Subramanian, et al. (2005) PNAS, 102(43):15545-15550) and GeneSetDB (Araki, et al. (2012) FEBS Open Bio, 2:76-82) collections.
	"""
	
	bioc = "EGSEAdata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/EGSEAdata_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/EGSEAdata/EGSEAdata_1.30.0.tar.gz"]

	version("1.36.0", tag="RELEASE_3_21")
	version("1.30.0", sha256="913ed4debf4ced5c7a5301e22bef10fd80c06b559f15609c748d85bf390e4854")

	depends_on("r@3.4:", type=("build", "run"))

