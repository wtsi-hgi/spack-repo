# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGms(RPackage):
	"""'GAMS' Modularization Support Package

	A collection of tools to create, use and maintain modularized model code written in the modeling 
    language 'GAMS' (<https://www.gams.com/>). Out-of-the-box 'GAMS' does not come with support for modularized
    model code. This package provides the tools necessary to convert a standard 'GAMS' model to a modularized one
    by introducing a modularized code structure together with a naming convention which emulates local
    environments. In addition, this package provides tools to monitor the compliance of the model code with
    modular coding guidelines.
	"""
	
	homepage = "https://github.com/pik-piam/gms"
	cran = "gms" 

	version("0.4.0", md5="7ad7c7e76dbcded65073bcf2905ab720")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
