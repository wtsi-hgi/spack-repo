# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REximir(RPackage):
	"""R functions for the normalization of Exiqon miRNA array data

	This package contains functions for reading raw data in ImaGene TXT format obtained from Exiqon miRCURY LNA arrays, annotating them with appropriate GAL files, and normalizing them using a spike-in probe-based method. Other platforms and data formats are also supported.
	"""
	
	bioc = "ExiMiR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ExiMiR_2.44.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ExiMiR/ExiMiR_2.44.0.tar.gz"]

	version("2.44.0", sha256="102d61cbd14f0bc6bd7ef8f20821396b56e0d878c74de02a59209521c2e76672")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-affy@1.26.1:", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-affyio@1.13.3:", type=("build", "run"))
	depends_on("r-preprocesscore@1.10:", type=("build", "run"))
