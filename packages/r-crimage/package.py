# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrimage(RPackage):
	"""CRImage a package to classify cells and calculate tumour cellularity

	CRImage provides functionality to process and analyze images, in particular to classify cells in biological images. Furthermore, in the context of tumor images, it provides functionality to calculate tumour cellularity.
	"""
	
	bioc = "CRImage"

	version("1.56.0", commit="78b37d2daa1c95ed5c7349391ca8985eb5b0eb7b")
	version("1.50.0", commit="8d8e44fd93e5199dc1620b15f0b33c50f57913c5")

	depends_on("r-ebimage", type=("build", "run"))
	depends_on("r-dnacopy", type=("build", "run"))
	depends_on("r-acgh", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-sgeostat", type=("build", "run"))
