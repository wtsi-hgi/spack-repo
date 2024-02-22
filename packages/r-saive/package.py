# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSaive(RPackage):
	"""Functions Used for SAiVE Group Research, Collaborations, and
Publications

	Holds functions developed by the University of Ottawa's SAiVE
    (Spatio-temporal Analysis of isotope Variations in the Environment)
    research group with the intention of facilitating the re-use of code,
    foster good code writing practices, and to allow others to benefit
    from the work done by the SAiVE group. Contributions are welcome via
    the 'GitHub' repository <https://github.com/UO-SAiVE/SAiVE> by group members as well as non-members.
	"""
	
	homepage = "https://github.com/UO-SAiVE/SAiVE"
	cran = "SAiVE" 

	version("1.0.4", md5="fe034e23191bc1a1f7e0cbc38c249979")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-vsurf", type=("build", "run"))
