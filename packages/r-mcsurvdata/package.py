# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcsurvdata(RPackage):
	"""Meta cohort survival data

	This package stores two merged expressionSet objects that contain the gene expression profile and clinical information of -a- six breast cancer cohorts and -b- four colorectal cancer cohorts. Breast cancer data are employed in the vignette of the hrunbiased package for survival analysis of gene signatures.
	"""
	
	homepage = "https://github.com/adricaba/mcsurvdata"
	bioc = "mcsurvdata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/mcsurvdata_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/mcsurvdata/mcsurvdata_1.20.0.tar.gz"]

	version("1.20.0", md5="0299258c7610f3675dc0b9f8e333eefa")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))

