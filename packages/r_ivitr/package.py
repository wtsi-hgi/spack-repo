# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIvitr(RPackage):
	"""Estimate IV-Optimal Individualized Treatment Rules

	A method that estimates
    an IV-optimal individualized treatment rule. An individualized
    treatment rule is said to be IV-optimal if it minimizes the 
    maximum risk with respect to the putative IV and the set of
    IV identification assumptions. Please refer to 
    <arXiv:2002.02579> for more details on the methodology and 
    some theory underpinning the method. Function IV-PILE() uses
    functions in the package 'locClass'. Package 'locClass' can be
    accessed and installed from the 'R-Forge' repository via the following link: 
    <https://r-forge.r-project.org/projects/locclass/>.
    Alternatively, one can install the package by entering the following in R:
    'install.packages("locClass", repos="<http://R-Forge.R-project.org>")'.
	"""
	
	cran = "ivitr" 

	version("0.1.0", md5="4984d868a79b37f9498d2293e1668a83")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
