# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWhatif(RPackage):
	"""Software for Evaluating Counterfactuals

	Inferences about counterfactuals are essential for prediction,
      answering what if questions, and estimating causal effects.
      However, when the counterfactuals posed are too far from the data at
      hand, conclusions drawn from well-specified statistical analyses
      become based largely on speculation hidden in convenient modeling
      assumptions that few would be willing to defend. Unfortunately,
      standard statistical approaches assume the veracity of the model
      rather than revealing the degree of model-dependence, which makes this
      problem hard to detect. WhatIf offers easy-to-apply methods to
      evaluate counterfactuals that do not require sensitivity testing over
      specified classes of models. If an analysis fails the tests offered
      here, then we know that substantive inferences will be sensitive to at
      least some modeling choices that are not based on empirical evidence,
      no matter what method of inference one chooses to use. WhatIf
      implements the methods for evaluating counterfactuals discussed in
      Gary King and Langche Zeng, 2006, "The Dangers of Extreme
      Counterfactuals," Political Analysis 14 (2) <DOI:10.1093/pan/mpj004>; 
      and Gary King and Langche Zeng, 2007, "When Can History Be Our Guide? The 
      Pitfalls of Counterfactual Inference," International Studies 
      Quarterly 51 (March) <DOI:10.1111/j.1468-2478.2007.00445.x>.
	"""
	
	homepage = "https://gking.harvard.edu/whatif"
	cran = "WhatIf" 

	version("1.5-10", md5="20ac8dcaa8788ebd020dcd578f5de4da")

	depends_on("r@2.3.1:", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-pbmcapply", type=("build", "run"))
