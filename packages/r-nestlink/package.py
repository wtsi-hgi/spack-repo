# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNestlink(RPackage):
	"""NestLink an R data package to guide through Engineered Peptide Barcodes for In-Depth Analyzes of Binding Protein Ensembles

	Provides next-generation sequencing (NGS) and mass spectrometry (MS) sample data, code snippets and replication material used for developing NestLink. The NestLink approach is a protein binder selection and identification technology able to biophysically characterize thousands of library members at once without handling individual clones at any stage of the process. Data were acquired on NGS and MS platforms at the Functional Genomics Center Zurich.
	"""
	
	bioc = "NestLink" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/NestLink_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/NestLink/NestLink_1.18.0.tar.gz"]

	version("1.18.0", md5="11cd94f5bd8b38cf261ae3346a283e81")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-annotationhub@2.15:", type=("build", "run"))
	depends_on("r-experimenthub@1:", type=("build", "run"))
	depends_on("r-biostrings@2.51:", type=("build", "run"))
	depends_on("r-gplots@3:", type=("build", "run"))
	depends_on("r-protviz@0.4:", type=("build", "run"))
	depends_on("r-shortread@1.41:", type=("build", "run"))

	# experiment