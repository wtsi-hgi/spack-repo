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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ASEB_1.46.3.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ASEB/ASEB_1.46.3.tar.gz"]

	version("1.52.0", tag="RELEASE_3_21")
	version("1.46.3", sha256="797561ff36b036921e82d824b4b3e7f81917229a361620951eb4141947a346b5")

	depends_on("r@2.8:", type=("build", "run"))
