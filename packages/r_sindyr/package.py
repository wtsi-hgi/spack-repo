# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSindyr(RPackage):
	"""Sparse Identification of Nonlinear Dynamics

	
    This implements the Brunton et al (2016; PNAS <doi:10.1073/pnas.1517384113>) sparse
    identification algorithm for finding ordinary differential equations for a measured 
    system from raw data (SINDy). The package includes a set of additional tools for 
    working with raw data, with an emphasis on cognitive science applications (Dale 
    and Bhat, in press <doi:10.1016/j.cogsys.2018.06.020>).
	"""
	
	cran = "sindyr" 

	version("0.2.3", md5="61238b5132ad57a81bbf33a4b49e74ed")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-arrangements", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-crqa", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
