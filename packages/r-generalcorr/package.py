# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeneralcorr(RPackage):
	"""Generalized Correlations, Causal Paths and Portfolio Selection

	Function gmcmtx0() computes a more reliable (general) 
    correlation matrix. Since causal paths from data are important for all sciences, the
    package provides many sophisticated functions. causeSummBlk() and causeSum2Blk()
    give easy-to-interpret causal paths.  Let Z denote control variables and compare 
    two flipped kernel regressions: X=f(Y, Z)+e1 and Y=g(X, Z)+e2. Our criterion Cr1 
    says that if |e1*Y|>|e2*X| then variation in X is more "exogenous or independent"
    than in Y, and the causal path is X to Y. Criterion Cr2 requires |e2|<|e1|. These
    inequalities between many absolute values are quantified by four orders of 
    stochastic dominance. Our third criterion Cr3, for the causal path X to Y,
    requires new generalized partial correlations to satisfy |r*(x|y,z)|< |r*(y|x,z)|.
    The function parcorVec() reports generalized partials between the first
    variable and all others.  The package provides several R functions including
    get0outliers() for outlier detection, bigfp() for numerical integration by the
    trapezoidal rule, stochdom2() for stochastic dominance, pillar3D() for 3D charts,
    canonRho() for generalized canonical correlations, depMeas() measures nonlinear
    dependence, and causeSummary(mtx) reports summary of causal paths among matrix 
    columns. Portfolio selection: decileVote(), momentVote(), dif4mtx(), exactSdMtx()
    can rank several stocks. Functions whose names begin with 'boot' provide bootstrap
    statistical inference, including a new bootGcRsq() test for "Granger-causality" 
    allowing nonlinear relations. A new tool for evaluation of out-of-sample
    portfolio performance is outOFsamp(). Panel data implementation is now included.
    See eight vignettes of the package for theory, examples, and
    usage tips. See Vinod (2019) doi{10.1080/03610918.2015.1122048}.
	"""
	
	cran = "generalCorr" 

	version("1.2.6", md5="359e6ec804bdc50cbf69c7fe83193601")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-np@0.60:", type=("build", "run"))
	depends_on("r-xtable@1.8:", type=("build", "run"))
	depends_on("r-meboot@1.4:", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
