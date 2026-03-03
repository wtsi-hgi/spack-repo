# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCat2cat(RPackage):
	"""Handling an Inconsistently Coded Categorical Variable in a
Longitudinal Dataset

	
    Unifying an inconsistently coded categorical variable between two different time points in accordance with a mapping table. 
    The main rule is to replicate the observation if it could be assigned to a few categories. 
    Then using frequencies or statistical methods to approximate the probabilities of being assigned to each of them. 
    This procedure was invented and implemented in the paper by Nasinski, Majchrowska, and Broniatowska (2020) <doi:10.24425/cejeme.2020.134747>.
	"""
	
	homepage = "https://github.com/Polkas/cat2cat"
	cran = "cat2cat" 

	version("0.4.7", md5="4bf9959e3702f54d368e1fcba0b04a3e")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
