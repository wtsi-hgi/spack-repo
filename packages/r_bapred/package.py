# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBapred(RPackage):
	"""Batch Effect Removal and Addon Normalization (in Phenotype
Prediction using Gene Data)

	Various tools dealing with batch effects, in particular enabling the 
  removal of discrepancies between training and test sets in prediction scenarios.
  Moreover, addon quantile normalization and addon RMA normalization (Kostka & Spang, 
  2008) is implemented to enable integrating the quantile normalization step into 
  prediction rules. The following batch effect removal methods are implemented: 
  FAbatch, ComBat, (f)SVA, mean-centering, standardization, Ratio-A and Ratio-G. 
  For each of these we provide  an additional function which enables a posteriori 
  ('addon') batch effect removal in independent batches ('test data'). Here, the
  (already batch effect adjusted) training data is not altered. For evaluating the
  success of batch effect adjustment several metrics are provided. Moreover, the 
  package implements a plot for the visualization of batch effects using principal 
  component analysis. The main functions of the package for batch effect adjustment 
  are ba() and baaddon() which enable batch effect removal and addon batch effect 
  removal, respectively, with one of the seven methods mentioned above. Another 
  important function here is bametric() which is a wrapper function for all implemented
  methods for evaluating the success of batch effect removal. For (addon) quantile 
  normalization and (addon) RMA normalization the functions qunormtrain(), 
  qunormaddon(), rmatrain() and rmaaddon() can be used.
	"""
	
	cran = "bapred" 

	version("1.1", md5="4c3d6358cc075e9ab376bb72635013af")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-sva", type=("build", "run"))
	depends_on("r-affyplm", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-fuzzyranktests", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
