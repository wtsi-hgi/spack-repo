# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBronchialil13(RPackage):
	"""time course experiment involving il13

	derived from CNMC (pepr.cnmcresearch.org) http://pepr.cnmcresearch.org/browse.do?action=list_prj_exp&projectId=95 Human Bronchial Cell line A549
	"""
	
	homepage = "http://www.biostat.harvard.edu/~carey"
	bioc = "bronchialIL13"

	version("1.46.0", commit="effb99266281d488ab9a018339ece5e5b8b01532")
	version("1.40.0", commit="7499106f124a6eba725f3382da7aea0a0f0f2d7b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-affy@1.23.4:", type=("build", "run"))

