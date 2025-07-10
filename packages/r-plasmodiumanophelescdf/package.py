# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlasmodiumanophelescdf(RPackage):
	"""plasmodiumanophelescdf

	A package containing an environment representing the Plasmodium_Anopheles.cdf file.
	"""
	
	bioc = "plasmodiumanophelescdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/plasmodiumanophelescdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/plasmodiumanophelescdf/plasmodiumanophelescdf_2.18.0.tar.gz"]

	version("2.18.0", sha256="09bb12c5b54d81e26a6292ad5fcc4025fae67af215ca6cdeb036ca16123043ef")

	depends_on("r-annotationdbi", type=("build", "run"))

