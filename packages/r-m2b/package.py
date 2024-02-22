# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RM2b(RPackage):
	"""Movement to Behaviour Inference using Random Forest

	Prediction of behaviour from movement 
	characteristics using observation and random forest for the analyses of movement
	data in ecology.
	From movement information (speed, bearing...) the model predicts the
	observed behaviour (movement, foraging...) using random forest. The
	model can then extrapolate behavioural information to movement data
	without direct observation of behaviours.
	The specificity of this method relies on the derivation of multiple predictor variables from the
	movement data over a range of temporal windows. This procedure allows to capture
	as much information as possible on the changes and variations of movement and
	ensures the use of the random forest algorithm to its best capacity. The method
	is very generic, applicable to any set of data providing movement data together with
	observation of behaviour.
	"""
	
	homepage = "https://github.com/ldbk/m2b"
	cran = "m2b" 

	version("1.0", md5="1420b9aecffaa89110e823f8a7ab04d7")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-catools", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
