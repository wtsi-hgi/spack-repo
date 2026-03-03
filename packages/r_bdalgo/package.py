# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBdalgo(RPackage):
	"""Bloom Detecting Algorithm

	The Bloom Detecting Algorithm enables the detection of blooms within a time series of species abundance and extracts 22 phenological variables. For details, see Karasiewicz et al. (2022) <doi:10.3390/jmse10020174>.
	"""
	
	cran = "BDAlgo" 

	version("0.1.0", md5="db6a3fb9174a621a0951ab44494c3661")

	depends_on("r-inflection", type=("build", "run"))
