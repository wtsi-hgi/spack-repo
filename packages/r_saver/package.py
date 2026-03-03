# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSaver(RPackage):
	"""Single-Cell RNA-Seq Gene Expression Recovery

	An implementation of a regularized regression prediction and 
    empirical Bayes method to recover the true gene expression profile in 
    noisy and sparse single-cell RNA-seq data. See Huang M, et al (2018) 
    <doi:10.1038/s41592-018-0033-z> for more details.
	"""
	
	homepage = "https://github.com/mohuangx/SAVER"
	cran = "SAVER" 

	version("1.1.2", md5="f4d3fea656db663d520f4478008c7660")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
