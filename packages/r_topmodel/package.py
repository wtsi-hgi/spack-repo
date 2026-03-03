# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTopmodel(RPackage):
	"""Implementation of the Hydrological Model TOPMODEL in R

	Set of hydrological functions including an R
        implementation of the hydrological model TOPMODEL, which is
        based on the 1995 FORTRAN version by Keith Beven. From version
        0.7.0, the package is put into maintenance mode.
	"""
	
	homepage = "https://github.com/ICHydro/topmodel"
	cran = "topmodel" 

	version("0.7.5", md5="1c8b418f473be4b3cc7734583056fb70")

