# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSgr(RPackage):
	"""Sample Generation by Replacement

	Sample Generation by Replacement simulations (SGR; Lombardi & Pastore, 2014; Pastore & Lombardi, 2014). The package can be used to perform fake data analysis according to the sample generation by replacement approach. It includes functions for making simple inferences about discrete/ordinal fake data. The package allows to study the implications of fake data for empirical results.
	"""
	
	cran = "sgr" 

	version("1.3.1", md5="b27da748b2caf04c97a0ad464e102610")

	depends_on("r-mass", type=("build", "run"))
