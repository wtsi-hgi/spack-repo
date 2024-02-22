# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPbd(RPackage):
	"""Protracted Birth-Death Model of Diversification

	Conducts maximum likelihood analysis and simulation of the
    protracted birth-death model of diversification. See
    Etienne, R.S. & J. Rosindell 2012 <doi:10.1093/sysbio/syr091>;
    Lambert, A., H. Morlon & R.S. Etienne 2014, <doi:10.1007/s00285-014-0767-x>;
    Etienne, R.S., H. Morlon & A. Lambert 2014, <doi:10.1111/evo.12433>.
	"""
	
	cran = "PBD" 

	version("1.4", md5="fe158203f91915ecf2f344f9438e3108")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-ddd", type=("build", "run"))
	depends_on("r-phytools", type=("build", "run"))
