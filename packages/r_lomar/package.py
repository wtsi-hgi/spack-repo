# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLomar(RPackage):
	"""Localization Microscopy Data Analysis

	Read, register and compare point sets from single molecule localization microscopy.
	"""
	
	homepage = "https://git.embl.de/heriche/lomar"
	cran = "LOMAR" 

	version("0.4.0", md5="2ba29a339f2754cc4335e2d84465b52b")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-transport", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-ff", type=("build", "run"))
	depends_on("r-aws", type=("build", "run"))
	depends_on("r-dbscan", type=("build", "run"))
	depends_on("r-ebimage", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-alphashape3d", type=("build", "run"))
	depends_on("r-bh@1.78.0.0:", type=("build", "run"))
	depends_on("gmp", type=("build", "link", "run"))
	depends_on("fftw@3:", type=("build", "link", "run"))
