# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcsw(RPackage):
	"""Inverse Compliance Score Weighting

	Provides the necessary tools to estimate average treatment effects with an instrumental variable by re-weighting observations using a model of compliance. 
	"""
	
	cran = "icsw" 

	version("1.0.0", md5="b7da5380952942de32a9e2fd49add087")

	depends_on("r@3:", type=("build", "run"))
