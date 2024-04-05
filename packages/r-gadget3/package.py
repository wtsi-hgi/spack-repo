# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGadget3(RPackage):
	"""Globally-Applicable Area Disaggregated General Ecosystem Toolbox
V3

	A framework to assist creation of marine ecosystem models,
             generating either 'R' or 'C++' code which can then be optimised using
             the 'TMB' package and standard 'R' tools. Principally designed to
             reproduce gadget2 models in 'TMB', but can be extended beyond
             gadget2's capabilities.
             Kasper Kristensen, Anders Nielsen, Casper W. Berg, Hans Skaug, Bradley M. Bell (2016) <doi:10.18637/jss.v070.i05> "TMB: Automatic Differentiation and Laplace Approximation.".
             Begley, J., & Howell, D. (2004) <https://core.ac.uk/download/pdf/225936648.pdf> "An overview of Gadget, the globally applicable area-disaggregated general ecosystem toolbox. ICES.".
	"""
	
	homepage = "https://gadget-framework.github.io/gadget3/"
	cran = "gadget3" 

	version("0.11-1", md5="72164af6f2cfa293a57b86088102e982", url="https://cran.r-project.org/src/contrib/gadget3_0.11-1.tar.gz")
	version("0.10-1", md5="5f3d3685c1c8f9af3c796cc7ca143d65", url="https://cran.r-project.org/src/contrib/gadget3_0.10-1.tar.gz")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-rlang@0.4.5:", type=("build", "run"))
	depends_on("r-tmb@1.7:", type=("build", "run"))
