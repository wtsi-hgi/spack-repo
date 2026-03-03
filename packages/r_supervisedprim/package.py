# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSupervisedprim(RPackage):
	"""Supervised Classification Learning and Prediction using Patient
Rule Induction Method (PRIM)

	The Patient Rule Induction Method (PRIM) is typically
  used for "bump hunting" data mining to identify regions with abnormally
  high concentrations of data with large or small values. This package
  extends this methodology so that it can be applied to binary classification
  problems and used for prediction.
	"""
	
	homepage = "https://github.com/dashaub/supervisedPRIM"
	cran = "supervisedPRIM" 

	version("2.0.0", md5="d16e5f76762eadca70dc55d0560db7bb")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-prim@1.0.16:", type=("build", "run"))
