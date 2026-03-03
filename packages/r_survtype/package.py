# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvtype(RPackage):
	"""Subtype Identification with Survival Data

	Subtypes are defined as groups of samples that have distinct molecular and clinical features. Genomic data can be analyzed for discovering patient subtypes, associated with clinical data, especially for survival information. This package is aimed to identify subtypes that are both clinically relevant and biologically meaningful.
	"""
	
	bioc = "survtype" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/survtype_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/survtype/survtype_1.18.0.tar.gz"]

	version("1.18.0", md5="e939bd3726a715cb0a817d0541ff86ab")

	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-survminer", type=("build", "run"))
	depends_on("r-clustvarsel", type=("build", "run"))
