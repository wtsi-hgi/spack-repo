# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPprep(RPackage):
	"""Analysis of Replication Studies using Power Priors

	Provides functionality for Bayesian analysis of replication studies using power prior approaches (Pawel et al., 2023) <doi:10.1007/s11749-023-00888-5>.
	"""
	
	homepage = "https://github.com/SamCH93/ppRep"
	cran = "ppRep" 

	version("0.42.3", md5="a0caec35b37f9600c8b241849014e45c")

	depends_on("r-hypergeo", type=("build", "run"))
