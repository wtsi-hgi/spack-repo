# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElec(RPackage):
	"""Collection of Functions for Statistical Election Audits

	This is a (somewhat bizarre) collection of functions written to do
        various sorts of statistical election audits.  There are also
        functions to generate simulated voting data, including methods to simulation different types 
        of voting errors which allow for simulations for checking the characteristics of
        these methods.
	"""
	
	cran = "elec" 

	version("0.1.2.2", md5="450544abaefb857dd4616144ac1f7b82")

	depends_on("r@2.10:", type=("build", "run"))
