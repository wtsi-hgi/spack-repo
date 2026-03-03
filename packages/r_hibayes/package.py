# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHibayes(RPackage):
	"""Individual-Level, Summary-Level and Single-Step Bayesian
Regression Model

	A user-friendly tool to fit Bayesian regression models. It can fit 3 types of Bayesian models using individual-level, summary-level, and individual plus pedigree-level (single-step) data for both Genomic prediction/selection (GS) and Genome-Wide Association Study (GWAS), it was designed to estimate joint effects and genetic parameters for a complex trait, including:
    (1) fixed effects and coefficients of covariates,
    (2) environmental random effects, and its corresponding variance, 
    (3) genetic variance, 
    (4) residual variance, 
    (5) heritability, 
    (6) genomic estimated breeding values (GEBV) for both genotyped and non-genotyped individuals,
    (7) SNP effect size, 
    (8) phenotype/genetic variance explained (PVE) for single or multiple SNPs, 
    (9) posterior probability of association of the genomic window (WPPA), 
    (10) posterior inclusive probability (PIP). 
    The functions are not limited, we will keep on going in enriching it with more features. 
    References: Meuwissen et al. (2001) <doi:10.1093/genetics/157.4.1819>; Gustavo et al. (2013) <doi:10.1534/genetics.112.143313>; Habier et al. (2011) <doi:10.1186/1471-2105-12-186>; Yi et al. (2008) <doi:10.1534/genetics.107.085589>; Zhou et al. (2013) <doi:10.1371/journal.pgen.1003264>; Moser et al. (2015) <doi:10.1371/journal.pgen.1004969>; Lloyd-Jones et al. (2019) <doi:10.1038/s41467-019-12653-0>; Henderson (1976) <doi:10.2307/2529339>; Fernando et al. (2014) <doi:10.1186/1297-9686-46-50>.
	"""
	
	homepage = "https://github.com/YinLiLin/hibayes"
	cran = "hibayes" 

	version("3.0.3", md5="7d16b77962c6cc9659fdf51e16d383d9")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-bigmemory", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-cmplot", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.9.600:", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
