# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTmti(RPackage):
	"""'Too Many, Too Improbable' (TMTI) Test Procedures

	Methods for computing joint tests, controlling the Familywise Error Rate (FWER) and getting lower bounds on the number of false hypotheses in a set. The methods implemented here are described in Mogensen and Markussen (2021) <arXiv:2108.04731>.
	"""
	
	cran = "TMTI" 

	version("1.0.1", md5="e8ca6c0ebcb93c66825bca25e98d1792")

	depends_on("r-rcpp", type=("build", "run"))
