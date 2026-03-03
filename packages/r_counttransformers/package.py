# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCounttransformers(RPackage):
	"""Transform Counts in RNA-Seq Data Analysis

	Provide data transformation functions to transform counts in RNA-seq data analysis. Please see the reference: Zhang Z, Yu D, Seo M, Hersh CP, Weiss ST, Qiu W. (2019) <doi.org/10.1038/s41598-019-41315-w>.
	"""
	
	cran = "countTransformers" 

	version("0.0.6", md5="2b960e9969c74cc7939737309f946f21")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
