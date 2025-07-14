# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowvs(RPackage):
	"""Variance stabilization in flow cytometry (and microarrays)

	Per-channel variance stabilization from a collection of flow cytometry samples by Bertlett test for homogeneity of variances. The approach is applicable to microarrays data as well.
	"""
	
	bioc = "flowVS"

	version("1.40.0", commit="19ad735f350c7e6eade574c26568daea6572554f")
	version("1.34.0", commit="3548b61f2e46a14a3ff3cefdb4daf6c2fd4bb4a4")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-flowviz", type=("build", "run"))
	depends_on("r-flowstats", type=("build", "run"))
