# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIccbin(RPackage):
	"""Facilitates Clustered Binary Data Generation, and Estimation of
Intracluster Correlation Coefficient (ICC) for Binary Data

	Assists in generating binary clustered data, estimates of Intracluster Correlation coefficient (ICC) for binary response in 16 different methods, and 5 different types of confidence intervals.
	"""
	
	homepage = "https://cran.r-project.org/package=ICCbin"
	cran = "ICCbin" 

	version("1.1.1", md5="02aeb144336a00609dd023e6405d9506")

