# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROssurvival(RPackage):
	"""Assessing Surrogacy with a Censored Outcome

	Identifies the optimal transformation of a surrogate marker and estimates the proportion of treatment explained (PTE) by the optimally-transformed surrogate at an earlier time point when the primary outcome of interest is a censored time-to-event outcome; details are described in Wang et al (2021) <doi:10.1002/sim.9185>.
	"""
	
	cran = "OSsurvival" 

	version("1.0", md5="b465a5873ed1b8467bdbcde7da5b17b5")

	depends_on("r@2.10:", type=("build", "run"))
