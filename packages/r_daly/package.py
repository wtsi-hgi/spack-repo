# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDaly(RPackage):
	"""The DALY Calculator - Graphical User Interface for Probabilistic
DALY Calculation in R

	The DALY Calculator is a free, open-source Graphical User
             Interface (GUI) for stochastic disability-adjusted life year
             (DALY) calculation.
	"""
	
	homepage = "http://daly.cbra.be"
	cran = "DALY" 

	version("1.5.0", md5="3aefa21f19512589b876e3e5f0ab09b6")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("tcl", type=("build", "link", "run"))
	depends_on("tk", type=("build", "link", "run"))
	depends_on("tktable", type=("build", "link", "run"))
