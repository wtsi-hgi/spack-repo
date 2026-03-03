# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModer(RPackage):
	"""Mode Estimation

	Determines single or multiple modes (most frequent values).
    Checks if missing values make this impossible, and returns 'NA'
    in this case. Dependency-free source code. See Franzese and Iuliano (2019)
    <doi:10.1016/B978-0-12-809633-8.20354-3>.
	"""
	
	homepage = "https://github.com/lhdjung/moder"
	cran = "moder" 

	version("0.2.1", md5="9d2fdba7264539c7fa9477daf49a269f")

