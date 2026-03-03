# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimrec(RPackage):
	"""Simulation of Recurrent Event Data for Non-Constant Baseline
Hazard

	Simulation of recurrent event data for non-constant baseline
    hazard in the total time model with risk-free intervals and possibly a competing event.
    Possibility to cut the data to an interim data set. Data can be plotted.
    Details about the method can be found in Jahn-Eimermacher, A. et al. (2015) <doi:10.1186/s12874-015-0005-2>.
	"""
	
	homepage = "https://github.com/federicomarini/simrec"
	cran = "simrec" 

	version("1.0.1", md5="90612741eb3e2118a496449429a9678a")

	depends_on("r@2.10:", type=("build", "run"))
