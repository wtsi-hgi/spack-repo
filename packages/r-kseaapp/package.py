# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKseaapp(RPackage):
	"""Kinase-Substrate Enrichment Analysis

	Infers relative kinase activity from phosphoproteomics data
    using the method described by Casado et al. (2013) <doi:10.1126/scisignal.2003573>.
	"""
	
	cran = "KSEAapp" 

	version("0.99.0", md5="82752bd1de1181d41e425465ff36c901")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
