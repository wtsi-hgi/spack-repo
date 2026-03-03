# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbf(RPackage):
	"""Robust Backfitting

	A robust backfitting algorithm for additive models based on (robust) local polynomial 
             kernel smoothers. It includes both bounded and re-descending (kernel) M-estimators, and
             it computes predictions for points outside the training set if desired. See
             Boente, Martinez and Salibian-Barrera (2017) <doi:10.1080/10485252.2017.1369077> and 
             Martinez and Salibian-Barrera (2021) <doi:10.21105/joss.02992> for details. 
	"""
	
	cran = "RBF" 

	version("2.1.1", md5="d0ac4768cb98d816a0d7dea5417f8134")

