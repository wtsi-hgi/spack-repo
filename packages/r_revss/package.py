# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRevss(RPackage):
	"""Robust Estimation in Very Small Samples

	Implements the estimation techniques described in Rousseeuw &
    Verboven (2002) <doi:10.1016/S0167-9473(02)00078-6> for the location and
    scale of very small samples.
	"""
	
	homepage = "https://github.com/aadler/revss"
	cran = "revss" 

	version("1.0.6", md5="723087d7497e0c6ab2edf06b6963df45")

