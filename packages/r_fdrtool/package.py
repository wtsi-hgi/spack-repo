# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFdrtool(RPackage):
	"""Estimation of (Local) False Discovery Rates and Higher Criticism

	Estimates both tail area-based false 
   discovery rates (Fdr) as well as local false discovery rates (fdr) for a 
   variety of null models (p-values, z-scores, correlation coefficients,
   t-scores).  The proportion of null values and the parameters of the null 
   distribution are adaptively estimated from the data.  In addition, the package 
   contains functions for non-parametric density estimation (Grenander estimator), 
   for monotone regression (isotonic regression and antitonic regression with weights),
   for computing the greatest convex minorant (GCM) and the least concave majorant (LCM), 
   for the half-normal and correlation distributions, and for computing
   empirical higher criticism (HC) scores and the corresponding decision threshold.
	"""
	
	homepage = "https://strimmerlab.github.io/software/fdrtool/"
	cran = "fdrtool" 

	version("1.2.17", md5="7e4ee6e67266b8828cc9d893a171545e")

	depends_on("r@3.0.2:", type=("build", "run"))
