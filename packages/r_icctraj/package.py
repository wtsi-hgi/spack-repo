# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcctraj(RPackage):
	"""Estimates the Intraclass Correlation Coefficient for Trajectory
Data

	Estimates the intraclass correlation coefficient for trajectory data using a matrix of distances between trajectories. The distances implemented are the extended Hausdorff distances (Min et al. 2007) <doi:10.1080/13658810601073315> and the discrete Fréchet distance (Magdy et al. 2015) <doi:10.1109/IntelCIS.2015.7397286>.
	"""
	
	cran = "iccTraj" 

	version("1.0.4", md5="079ea0232abba348ce5da1a0aa383ff9")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magic", type=("build", "run"))
	depends_on("r-trajectories", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-spacetime", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
