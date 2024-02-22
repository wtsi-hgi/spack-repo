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
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/gwascatData_0.99.6.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/gwascatData/gwascatData_0.99.6.tar.gz"]

	version("0.99.6", md5="fa09db539ac0a16ba136e810a5b9970a")

	depends_on("r-data-table", type=("build", "run"))

	# annotation