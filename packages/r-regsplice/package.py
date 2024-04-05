# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRegsplice(RPackage):
	"""L1-regularization based methods for detection of differential splicing

	Statistical methods for detection of differential splicing (differential exon usage) in RNA-seq and exon microarray data, using L1-regularization (lasso) to improve power.
	"""
	
	homepage = "https://github.com/lmweber/regsplice"
	bioc = "regsplice" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/regsplice_1.28.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/regsplice/regsplice_1.28.1.tar.gz"]

	version("1.28.1", md5="eaeba7b7629e9360cc51c11c611499c5")
	version("1.28.0", md5="3f63d2e93b02aec3ed044e2c56938d12")

	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
