# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHtrx(RPackage):
	"""Haplotype Trend Regression with eXtra Flexibility (HTRX)

	Detection of haplotype patterns that include single nucleotide polymorphisms (SNPs) and non-contiguous haplotypes that are associated with a phenotype. Methods for implementing HTRX are described in Yang Y, Lawson DJ (2023) <doi:10.1093/bioadv/vbad038> and Barrie W, Yang Y, Irving-Pease E.K, et al (2024) <doi:10.1038/s41586-023-06618-z>.
	"""
	
	cran = "HTRX" 

	version("1.2.4", md5="d277c0f6350c5ecf2499b0d90a9e561a")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-fastglm", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-tune", type=("build", "run"))
	depends_on("r-recipes", type=("build", "run"))
