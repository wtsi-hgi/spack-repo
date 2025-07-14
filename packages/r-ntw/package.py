# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNtw(RPackage):
	"""Predict gene network using an Ordinary Differential Equation (ODE) based method

	This package predicts the gene-gene interaction network and identifies the direct transcriptional targets of the perturbation using an ODE (Ordinary Differential Equation) based method.
	"""
	
	bioc = "NTW" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/NTW_1.52.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/NTW/NTW_1.52.0.tar.gz"]

	version("1.58.0", tag="RELEASE_3_21")
	version("1.52.0", sha256="da9c5ec5e59c7b7a648ed694fbde2b67365eeb747322e2ca73bf0321ee3f629c")

	depends_on("r@2.3:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
