# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMltest(RPackage):
	"""Classification Evaluation Metrics

	A fast, robust and easy-to-use calculation of multi-class classification evaluation metrics based on confusion matrix.
	"""
	
	cran = "mltest" 

	version("1.0.1", md5="29b8905d07ae4f377b53396d8d0d2956")

