# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCancerdata(RPackage):
	"""Development and validation of diagnostic tests from high-dimensional molecular data: Datasets

	Dataset for the R package cancerclass
	"""
	
	bioc = "cancerdata"

	version("1.46.0", commit="fc32f06ad646da4f2218b86e12191b17b249c829")
	version("1.40.0", commit="83e46f593472929f7e0d0378a68abe27ec359c2f")

	depends_on("r@2.10.1:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))

