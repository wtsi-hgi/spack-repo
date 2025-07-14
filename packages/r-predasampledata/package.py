# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPredasampledata(RPackage):
	"""expression and copy number data on clear cell renal carcinoma samples

	Sample data for PREDA package. (annotations objects synchronized with GeneAnnot custom CDFs version 2.2.0)
	"""
	
	bioc = "PREDAsampledata"

	version("0.48.0", commit="dca0d312a2c734671780ebf40498f832edf5a198")
	version("0.42.0", commit="cab6a54cce6c6bb0ac275a722816d47d32d8bf40")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-preda", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-annotate", type=("build", "run"))

