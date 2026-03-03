# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmoajars(RPackage):
	"""External jars Required for Package RMOA

	External jars required for package RMOA. RMOA is a framework to
    build data stream models on top of MOA (Massive Online Analysis -
    <https://moa.cms.waikato.ac.nz/>). The jar files are put in this R package, the modelling logic can be found in the RMOA package.
	"""
	
	homepage = "https://moa.cms.waikato.ac.nz/"
	cran = "RMOAjars" 

	version("1.2.0", md5="e7f01a2acdc557f994bbc818fac14c58")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-rjava@1.0.1:", type=("build", "run"))
	depends_on("openjdk@5:", type=("build", "link", "run"))
