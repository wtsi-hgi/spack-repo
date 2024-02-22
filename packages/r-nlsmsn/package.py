# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlsmsn(RPackage):
	"""Fitting Nonlinear Models with Scale Mixture of Skew-Normal
Distributions

	Fit univariate non-linear scale mixture of skew-normal(NL-SMSN) regression, details in Garay, Lachos and Abanto-Valle (2011) <doi:10.1016/j.jkss.2010.08.003> and Lachos, Bandyopadhyay and Garay (2011) <doi:10.1016/j.spl.2011.03.019>.
	"""
	
	cran = "nlsmsn" 

	version("0.0-6", md5="40fc3eaaae97c5776310b20378c64384")

	depends_on("r@2.10:", type=("build", "run"))
