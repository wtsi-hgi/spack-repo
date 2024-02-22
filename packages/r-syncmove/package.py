# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSyncmove(RPackage):
	"""Subsample Temporal Data to Synchronal Events and Compute the MCI

	The function 'syncSubsample' subsamples temporal data of different entities so that the result only contains synchronal events. The function 'mci' calculates the Movement Coordination Index (MCI, see reference on help page for function 'mci') of a data set created with the function 'syncSubsample'.
	"""
	
	cran = "SyncMove" 

	version("0.1-0", md5="4536122c1b90a11df08372f5385c2529")

	depends_on("r@3.1:", type=("build", "run"))
