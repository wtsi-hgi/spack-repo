# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPedalfastData(RPackage):
	"""PEDALFAST Data

	Data files and documentation for PEDiatric vALidation oF vAriableS
    in TBI (PEDALFAST).  The data was used in "Functional Status Scale in
    Children With Traumatic Brain Injury: A Prospective Cohort Study" by Bennett,
    Dixon, et al  (2016) <doi:10.1097/PCC.0000000000000934>.
	"""
	
	cran = "pedalfast.data" 

	version("1.0.1", md5="56ad9c7795add77619294898a89a6f1e")

	depends_on("r@3.5:", type=("build", "run"))
