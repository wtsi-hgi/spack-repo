# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REffecttreat(RPackage):
	"""Prediction of Therapeutic Success

	In personalized medicine, one wants to know, for a given patient and his or her outcome for a predictor (pre-treatment variable), how likely it is that a treatment will be more beneficial than an alternative treatment. This package allows for the quantification of the predictive causal association (i.e., the association between the predictor variable and the individual causal effect of the treatment) and related metrics. Part of this software has been developed using funding provided from the European Union's 7th Framework Programme for research, technological development and demonstration under Grant Agreement no 602552.
	"""
	
	cran = "EffectTreat" 

	version("1.1", md5="bbc74383a1dc43f3aa81a04d2aa8153c")

