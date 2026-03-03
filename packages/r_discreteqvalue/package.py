# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiscreteqvalue(RPackage):
	"""Improved q-Values for Discrete Uniform and Homogeneous Tests

	We consider a multiple testing procedure used in many modern applications which is the q-value method proposed by Storey and Tibshirani (2003), <doi:10.1073/pnas.1530509100>. The q-value method is based on the false discovery rate (FDR), hence versions of the q-value method can be defined depending on which estimator of the proportion of true null hypotheses, p0, is plugged in the FDR estimator. We implement the q-value method based on two classical pi0 estimators, and furthermore, we propose and implement three versions of the q-value method for homogeneous discrete uniform P-values based on pi0 estimators which take into account the discrete distribution of the P-values.
	"""
	
	cran = "DiscreteQvalue" 

	version("1.1", md5="805364abc4b465b67fdda443dd95f5e8")

