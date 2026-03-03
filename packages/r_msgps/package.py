# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsgps(RPackage):
	"""Degrees of Freedom of Elastic Net, Adaptive Lasso and
Generalized Elastic Net

	Computes the degrees of freedom of the lasso,
        elastic net, generalized elastic net and adaptive lasso based
        on the generalized path seeking algorithm.  The optimal model
        can be selected by model selection criteria including Mallows'
        Cp, bias-corrected AIC (AICc), generalized cross validation
        (GCV) and BIC.
	"""
	
	homepage = "https://keihirose.com/"
	cran = "msgps" 

	version("1.3.5", md5="96879aeb565fb24de9bfd14cd333a2cf")

