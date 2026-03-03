# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLineup(RPackage):
	"""Lining Up Two Sets of Measurements

	Tools for detecting and correcting sample mix-ups between two sets
    of measurements, such as between gene expression data on two tissues.
    Broman et al. (2015) <doi:10.1534/g3.115.019778>.
	"""
	
	homepage = "https://github.com/kbroman/lineup"
	cran = "lineup" 

	version("0.42", md5="af1e27c35f527c00d4da47ef2fb87b8e")

	depends_on("r@2.10.1:", type=("build", "run"))
	depends_on("r-qtl@1.20.15:", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
