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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/flowVS_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/flowVS/flowVS_1.34.0.tar.gz"]

	version("1.40.0", tag="RELEASE_3_21")
	version("1.34.0", sha256="1ab7defff0cbebf8f71dee48ae95426546f31277ed929022ab36b9283bbf54a6")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-flowviz", type=("build", "run"))
	depends_on("r-flowstats", type=("build", "run"))
