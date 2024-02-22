# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrm(RPackage):
	"""Continual Reassessment Method (CRM) for Phase I Clinical Trials

	Functions for phase I clinical trials using the continual reassessment method.
	"""
	
	cran = "CRM" 

	version("1.2.4", md5="c9ceb2e6673a785d02f59f62cd35a206")

	depends_on("r@2.10:", type=("build", "run"))
