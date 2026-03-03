# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLipidms(RPackage):
	"""Lipid Annotation for LC-MS/MS DDA or DIA Data

	Lipid annotation in untargeted LC-MS lipidomics based on fragmentation rules. Alcoriza-Balaguer MI, Garcia-Canaveras JC, Lopez A, Conde I, Juan O, Carretero J, Lahoz A (2019) <doi:10.1021/acs.analchem.8b03409>.
	"""
	
	cran = "LipidMS" 

	version("3.0.4", md5="b50a5c7c2807e4198f659c505b5e1351")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-readmzxmldata", type=("build", "run"))
	depends_on("r-chnosz", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
