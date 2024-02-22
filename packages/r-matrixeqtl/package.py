# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatrixeqtl(RPackage):
	"""Matrix eQTL: Ultra Fast eQTL Analysis via Large Matrix
Operations

	Matrix eQTL is designed for fast eQTL analysis on large datasets.
        Matrix eQTL can test for association between genotype 
        and gene expression using linear regression 
        with either additive or ANOVA genotype effects.
        The models can include covariates to account for factors 
        as population stratification, gender, and clinical variables. 
        It also supports models with heteroscedastic and/or correlated errors,
        false discovery rate estimation and 
        separate treatment of local (cis) and distant (trans) eQTLs.
        For more details see Shabalin (2012) <doi:10.1093/bioinformatics/bts163>.
	"""
	
	homepage = "http://www.bios.unc.edu/research/genomic_software/Matrix_eQTL/"
	cran = "MatrixEQTL" 

	version("2.3", md5="a0fef869db8c28dc36a72fe62afd1309")

	depends_on("r@2.12:", type=("build", "run"))
