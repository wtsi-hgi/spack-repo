# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAmelie(RPackage):
	"""Anomaly Detection with Normal Probability Functions

	Implements anomaly detection as binary classification for cross-sectional data. Uses maximum likelihood estimates and normal probability functions to classify observations as anomalous. The method is presented in the following lecture from the Machine Learning course by Andrew Ng: <https://www.coursera.org/learn/machine-learning/lecture/C8IJp/algorithm/>, and is also described in: Aleksandar Lazarevic, Levent Ertoz, Vipin Kumar, Aysel Ozgur, Jaideep Srivastava (2003) <doi:10.1137/1.9781611972733.3>.
	"""
	
	cran = "amelie" 

	version("0.2.1", md5="2647d5d2e2cf4cfcded3c77956a85f1b")

