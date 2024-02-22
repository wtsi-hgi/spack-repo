# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REeptools(RPackage):
	"""Convenience Functions for Education Data

	Collection of convenience functions to make working with
    administrative records easier and more consistent. Includes functions to
    clean strings, and identify cut points. Also includes three example data 
    sets of administrative education records for learning how to process records 
    with errors.
	"""
	
	homepage = "https://github.com/jknowles/eeptools"
	cran = "eeptools" 

	version("1.2.5", md5="bb953008ab2dba0ebbdb25252a6cfb7f")

	depends_on("r@3.5.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-arm", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-vcd", type=("build", "run"))
