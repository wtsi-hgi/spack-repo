# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHum(RPackage):
	"""Compute HUM Value and Visualize ROC Curves

	Tools for computing HUM (Hypervolume Under the Manifold) value to estimate features ability
             to discriminate the class labels, visualizing the ROC curve for two or three class labels
             (Natalia Novoselova, Cristina Della Beffa, Junxi Wang, Jialiang Li, Frank Pessler, Frank Klawonn
             (2014) <doi:10.1093/bioinformatics/btu086>).
	"""
	
	homepage = "https://public.ostfalia.de/~klawonn/HUM.htm"
	cran = "HUM" 

	version("2.0", md5="16bc6ae2d63a0d518e4eb21e80dd5d4d")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
