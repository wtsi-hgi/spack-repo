# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGwascatdata(RPackage):
	"""A text file in cloud with March 30 2021 snapshot of EBI/EMBL GWAS catalog

	This package manages a text file in cloud with March 30 2021 snapshot of EBI/EMBL GWAS catalog.This simplifies access to a snapshot of EBI GWASCAT.  More current images can be obtained using the gwascat package.
	"""
	
	bioc = "gwascatData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/gwascatData_0.99.6.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/gwascatData/gwascatData_0.99.6.tar.gz"]

    version("0.99.6", tag="RELEASE_3_21")
	version("0.99.6", sha256="ea3d16210eb7c7ea22916568279fe4c750bc091b181818404778c76d00fd15f6")

	depends_on("r-data-table", type=("build", "run"))

