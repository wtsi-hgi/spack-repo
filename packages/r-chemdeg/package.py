# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChemdeg(RPackage):
	"""Analysis of Chemical Degradation Kinetic Data

	A collection of functions that have been developed to assist
    experimenter in modeling chemical degradation kinetic data. The
    selection of the appropriate degradation model and parameter
    estimation is carried out automatically as far as possible and is
    driven by a rigorous statistical interpretation of the results.  The
    package integrates already available goodness-of-fit statistics for
    nonlinear models. In addition it allows data fitting with the
    nonlinear first-order multi-target (FOMT) model.
	"""
	
	homepage = "https://github.com/migliomatte/chemdeg"
	cran = "chemdeg" 

	version("0.1.2", md5="285e3adc74efa3974f33f4f131f3a1ec")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
