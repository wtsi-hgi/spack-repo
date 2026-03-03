# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAutoensemble(RPackage):
	"""Automated Stacked Ensemble Classifier for Severe Class Imbalance

	An AutoML algorithm is developed to construct homogeneous or 
             heterogeneous stacked ensemble models using specified base-learners. 
             Various criteria are employed to identify optimal models, enhancing 
             diversity among them and resulting in more robust stacked ensembles. 
             The algorithm optimizes the model by incorporating an increasing 
             number of top-performing models to create a diverse combination. 
             Presently, only models from 'h2o.ai' are supported.
	"""
	
	homepage = "https://github.com/haghish/autoEnsemble"
	cran = "autoEnsemble" 

	version("0.2", md5="adef01747a667620de9dce0308d6f65c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-h2o@3.34:", type=("build", "run"))
	depends_on("r-h2otools@0.3:", type=("build", "run"))
	depends_on("r-curl@4.3:", type=("build", "run"))
