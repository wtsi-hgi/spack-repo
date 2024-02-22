# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAseb(RPackage):
	"""Predict Acetylated Lysine Sites

	ASEB is an R package to predict lysine sites that can be acetylated by a specific KAT-family.
	"""
	
	bioc = "ASEB" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/ASEB_1.46.3.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/ASEB/ASEB_1.46.3.tar.gz"]

	version("1.46.3", md5="7e9312371523d44d7f1cb759af2d150e")

	depends_on("r@2.8:", type=("build", "run"))
