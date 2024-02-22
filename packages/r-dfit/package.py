# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDfit(RPackage):
	"""Differential Functioning of Items and Tests

	A set of functions to perform Raju, van der Linden and Fleer's
    (1995, <doi:10.1177/014662169501900405>) Differential Functioning of Items
    and Tests (DFIT) analyses. It includes functions to use the Monte Carlo Item
    Parameter Replication approach (Oshima, Raju, & Nanda, 2006, <doi:10.1111/j.1745-3984.2006.00001.x>)
    for obtaining the associated statistical significance
    tests cut-off points. They may also be used for a priori and post-hoc power
    calculations (Cervantes, 2017, <doi:10.18637/jss.v076.i05>).
	"""
	
	cran = "DFIT" 

	version("1.1", md5="ef7a2b58c0daec675460570e5792a347")

	depends_on("r-msm", type=("build", "run"))
	depends_on("r-mirt", type=("build", "run"))
	depends_on("r-simex", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
