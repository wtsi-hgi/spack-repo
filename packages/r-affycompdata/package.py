# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAffycompdata(RPackage):
	"""affycomp data

	Data needed by the affycomp package.
	"""
	
	homepage = "https://bioconductor.org/packages/affycompData"
	bioc = "affycompData"

	version("1.46.0", commit="ec031441e4a6e0c22f9eab7545427d66f6de1fb3")
	version("1.40.0", commit="3b9531571bb8445e063a284aad9068dc391b1652")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-biobase@2.3.3:", type=("build", "run"))
	depends_on("r-affycomp", type=("build", "run"))

