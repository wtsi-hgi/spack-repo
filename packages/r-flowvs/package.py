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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/flowVS_1.34.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/flowVS/flowVS_1.34.0.tar.gz"]

	version("1.34.0", md5="43fc57f2be5ccbfcff9ac9b9bc0bb857")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-flowviz", type=("build", "run"))
	depends_on("r-flowstats", type=("build", "run"))
