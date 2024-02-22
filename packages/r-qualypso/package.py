# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQualypso(RPackage):
	"""Partitioning Uncertainty Components of an Incomplete Ensemble of
Climate Projections

	These functions use data augmentation and Bayesian techniques for the assessment of single-member and incomplete ensembles of climate projections. It provides unbiased estimates of climate change responses of all simulation chains and of all uncertainty variables. It additionally propagates uncertainty due to missing information in the estimates.
  - Evin, G., B. Hingray, J. Blanchet, N. Eckert, S. Morin, and D. Verfaillie. (2019) <doi:10.1175/JCLI-D-18-0606.1>.
	"""
	
	cran = "QUALYPSO" 

	version("2.3", md5="3f524ac993f053905796feeda58a407a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
