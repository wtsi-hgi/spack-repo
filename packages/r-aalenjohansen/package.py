# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAalenjohansen(RPackage):
	"""Conditional Aalen-Johansen Estimation

	Provides the conditional Nelson-Aalen and Aalen-Johansen estimators. The methods are based on Bladt & Furrer (2023), in preparation.
	"""
	
	cran = "AalenJohansen" 

	version("1.0", md5="d7eb2a6275daa6af43bf8a980398b312")

