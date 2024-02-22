# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDamr(RPackage):
	"""Interface to Drosophila Activity Monitor System Result Files

	Loads behavioural data from the widely used Drosophila Activity Monitor System (DAMS, TriKinetics <https://trikinetics.com/>) into the rethomics framework.
	"""
	
	homepage = "https://github.com/rethomics/damr"
	cran = "damr" 

	version("0.3.7", md5="9dc1ebb3f4f102bf5cc4974089ad74f7")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-behavr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
