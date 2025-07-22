# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProlocdata(RPackage):
	"""Data accompanying the pRoloc package

	Mass-spectrometry based spatial proteomics data sets and protein complex separation data. Also contains the time course expression experiment from Mulvey et al. 2015.
	"""
	
	homepage = "https://github.com/lgatto/pRolocdata"
	bioc = "pRolocdata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/pRolocdata_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/pRolocdata/pRolocdata_1.40.0.tar.gz"]

    version("1.46.0", tag="RELEASE_3_21")
	version("1.40.0", sha256="f1c405105a5ea16a4343112d710842065722c6a773db904d6bbea789ced15e7e")

	depends_on("r@3.6.3:", type=("build", "run"))
	depends_on("r-msnbase", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))

