# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAmmistability(RPackage):
	"""Additive Main Effects and Multiplicative Interaction Model
Stability Parameters

	Computes various stability parameters from Additive Main Effects
    and Multiplicative Interaction (AMMI) analysis results such as  Modified
    AMMI Stability Value (MASV), Sums of the Absolute Value of the Interaction
    Principal Component Scores (SIPC), Sum Across Environments of
    Genotype-Environment Interaction Modelled by AMMI (AMGE), Sum Across 
    Environments of Absolute Value of Genotype-Environment Interaction Modelled
    by AMMI (AV_(AMGE)), AMMI Stability Index (ASI), Modified ASI (MASI), AMMI
    Based Stability Parameter (ASTAB), Annicchiarico's D Parameter (DA), Zhang's
    D Parameter (DZ), Averages of the Squared Eigenvector Values (EV), Stability
    Measure Based on Fitted AMMI Model (FA), Absolute Value of the Relative
    Contribution of IPCs to the Interaction (Za). Further calculates the
    Simultaneous Selection Index for Yield and Stability from the computed
    stability parameters. See the vignette for complete list of citations for
    the methods implemented.
	"""
	
	homepage = "https://github.com/ajaygpb/ammistability/"
	cran = "ammistability" 

	version("0.1.4", md5="eed56420d6d3a327ab86c44d42595d20")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-agricolae", type=("build", "run"))
	depends_on("r-ggcorrplot", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
