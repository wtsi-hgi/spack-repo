# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROscillatorgenerator(RPackage):
	"""Generation of Customizable, Discretized Time Series of
Oscillating Species

	The supplied code allows for the generation of discrete time series of oscillating species. General shapes can be selected by means of individual functions, which are widely customizable by means of function arguments. All code was developed in the Biological Information Processing Group at the BioQuant Center at Heidelberg University, Germany.
	"""
	
	cran = "OscillatorGenerator" 

	version("0.1.0", md5="7efea34e47c06572126c06418659b040")

	depends_on("r@3.4:", type=("build", "run"))
