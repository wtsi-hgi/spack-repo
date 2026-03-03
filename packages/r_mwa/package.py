# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMwa(RPackage):
	"""Causal Inference in Spatiotemporal Event Data

	Implementation of Matched Wake Analysis (mwa) for studying causal relationships in spatiotemporal event data, introduced by Schutte and Donnay (2014) <doi:10.1016/j.polgeo.2014.03.001>. 
	"""
	
	cran = "mwa" 

	version("0.4.4", md5="0f6828f6494843a1c943ebab6a9a9ca0")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-cem@1.1:", type=("build", "run"))
	depends_on("r-rjava@0.9:", type=("build", "run"))
	depends_on("r-mass@7:", type=("build", "run"))
	depends_on("openjdk@1.6:", type=("build", "link", "run"))
