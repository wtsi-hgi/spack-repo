# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCampsismod(RPackage):
	"""Generic Implementation of a PK/PD Model

	A generic, easy-to-use and expandable implementation of a
    pharmacokinetic (PK) / pharmacodynamic (PD) model based on the S4
    class system. This package allows the user to read/write a
    pharmacometric model from/to files and adapt it further on the fly in
    the R environment. For this purpose, this package provides an
    intuitive API to add, modify or delete equations, ordinary
    differential equations (ODE's), model parameters or compartment
    properties (like infusion duration or rate, bioavailability and
    initial values). Finally, this package also provides a useful export
    of the model for use with simulation packages 'rxode2' and 'mrgsolve'.
    This package is designed and intended to be used with package
    'campsis', a PK/PD simulation platform built on top of 'rxode2' and
    'mrgsolve'.
	"""
	
	homepage = "https://github.com/Calvagone/campsismod"
	cran = "campsismod" 

	version("1.1.1", md5="98d0199f622a7c9ea38782d435329a3c")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
