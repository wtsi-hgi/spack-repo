# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProporz(RPackage):
	"""Proportional Apportionment

	Calculate seat apportionment for legislative bodies with 
    various methods. The algorithms include divisor or highest averages methods
    (e.g. Jefferson, Webster or Adams), largest remainder methods and 
    biproportional apportionment.
    Gaffke, N. & Pukelsheim, F. (2008) <doi:10.1016/j.mathsocsci.2008.01.004>
    Oelbermann, K. F. (2016) <doi:10.1016/j.mathsocsci.2016.02.003>.
	"""
	
	homepage = "https://github.com/polettif/proporz"
	cran = "proporz" 

	version("1.4.0", md5="0427a416539d5441a5d3a913128c82dc")

	depends_on("r@3.6:", type=("build", "run"))
