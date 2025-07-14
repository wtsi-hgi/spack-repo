# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdisop(RPackage):
	"""Decomposition of Isotopic Patterns

	Identification of metabolites using high precision mass spectrometry. MS Peaks are used to derive a ranked list of sum formulae, alternatively for a given sum formula the theoretical isotope distribution can be calculated to search in MS peak lists.
	"""
	
	homepage = "https://github.com/sneumann/Rdisop"
	bioc = "Rdisop" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Rdisop_1.62.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Rdisop/Rdisop_1.62.0.tar.gz"]

	version("1.68.0", tag="RELEASE_3_21")
	version("1.62.0", sha256="0600d03ab393b592604865b2ac42e11aa6c09fb2d3978b3ac679e5ace130e0cb")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
