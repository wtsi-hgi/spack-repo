# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDcgsa(RPackage):
	"""Distance-correlation based Gene Set Analysis for longitudinal gene expression profiles

	Distance-correlation based Gene Set Analysis for longitudinal gene expression profiles. In longitudinal studies, the gene expression profiles were collected at each visit from each subject and hence there are multiple measurements of the gene expression profiles for each subject. The dcGSA package could be used to assess the associations between gene sets and clinical outcomes of interest by fully taking advantage of the longitudinal nature of both the gene expression profiles and clinical outcomes.
	"""
	
	bioc = "dcGSA" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/dcGSA_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/dcGSA/dcGSA_1.30.0.tar.gz"]

	version("1.36.0", tag="RELEASE_3_21")
	version("1.30.0", sha256="d1703121d076b5ed0096104a3769f9eaab7d6f3e044ff8a78aa1d5f3105b0322")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
