# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlgem(RPackage):
	"""Detect differential expression in microarray and proteomics datasets with the Power Law Global Error Model (PLGEM)

	The Power Law Global Error Model (PLGEM) has been shown to faithfully model the variance-versus-mean dependence that exists in a variety of genome-wide datasets, including microarray and proteomics data. The use of PLGEM has been shown to improve the detection of differentially expressed genes or proteins in these datasets.
	"""
	
	homepage = "http://www.genopolis.it"
	bioc = "plgem" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/plgem_1.74.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/plgem/plgem_1.74.0.tar.gz"]

    version("1.80.0", tag="RELEASE_3_21")
	version("1.74.0", sha256="efe1a7ce154f64857494fa95d8be80da6c32a0fe2533aed403b1b5dd878ab068")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
