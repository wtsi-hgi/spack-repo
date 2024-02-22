# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPbm(RPackage):
	"""Protein Binding Models

	Binding models which are useful when analysing protein-ligand interactions by techniques such as Biolayer Interferometry (BLI) or Surface Plasmon Resonance (SPR). Naman B. Shah, Thomas M. Duncan (2014) <doi:10.3791/51383>. Hoang H. Nguyen et al. (2015) <doi:10.3390/s150510481>. After initial binding parameters are known, binding curves can be simulated and parameters can be varied. The models within this package may also be used to fit a curve to measured binding data using non-linear regression.
	"""
	
	homepage = "https://github.com/jonathanrd/pbm"
	cran = "pbm" 

	version("1.2.1", md5="da9f166eaf69acc29350fade7234ae7d")

	depends_on("r@3.4.4:", type=("build", "run"))
