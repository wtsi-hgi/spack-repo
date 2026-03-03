# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDosresmeta(RPackage):
	"""Multivariate Dose-Response Meta-Analysis

	Estimates dose-response relations from summarized dose-response
    data and to combines them according to principles of (multivariate)
    random-effects models.  
	"""
	
	homepage = "https://alecri.github.io/software/dosresmeta.html"
	cran = "dosresmeta" 

	version("2.0.1", md5="e058c6d9666893a7d92d36fc0041d90a")

	depends_on("r-mvmeta", type=("build", "run"))
