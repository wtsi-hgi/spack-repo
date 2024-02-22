# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSynth(RPackage):
	"""Synthetic Control Group Method for Comparative Case Studies

	Implements the synthetic control group method for comparative case studies as described in Abadie and Gardeazabal (2003) and Abadie, Diamond, and Hainmueller (2010, 2011, 2014). The synthetic control method allows for effect estimation in settings where a single unit (a state, country, firm, etc.) is exposed to an event or intervention. It provides a data-driven procedure to construct synthetic control units based on a weighted combination of comparison units that approximates the characteristics of the unit that is exposed to the intervention. A combination of comparison units often provides a better comparison for the unit exposed to the intervention than any comparison unit alone.
	"""
	
	homepage = "https://web.stanford.edu/~jhain/"
	cran = "Synth" 

	version("1.1-8", md5="2bcc5f8c6861666d62b5f4cf7969dbd2")

	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
	depends_on("r-rgenoud", type=("build", "run"))
