# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REbal(RPackage):
	"""Entropy Reweighting to Create Balanced Samples

	Package implements entropy balancing, a data preprocessing procedure described in Hainmueller (2008, <doi:10.1093/pan/mpr025>) that allows users to reweight a dataset such that the covariate distributions in the reweighted data satisfy a set of user specified moment conditions. This can be useful to create balanced samples in observational studies with a binary treatment where the control group data can be reweighted to match the covariate moments in the treatment group. Entropy balancing can also be used to reweight a survey sample to known characteristics from a target population.
	"""
	
	homepage = "https://web.stanford.edu/~jhain/"
	cran = "ebal" 

	version("0.1-8", md5="50283d2406f9943623f8d9dda67b4b77")

