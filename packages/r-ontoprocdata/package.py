# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROntoprocdata(RPackage):
	"""A data package for ontoProc

	This package manages rda files of multiple ontologies that are used in the ontoProc package. These ontologies were originally downloaded as owl or obo files and converted into Rda files. The files were downloaded at various times but most of them were downloaded on August 08 2022.
	"""
	
	bioc = "ontoProcData" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/ontoProcData_0.99.9901.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/ontoProcData/ontoProcData_0.99.9901.tar.gz"]

	version("0.99.9901", md5="d4160c1fc853db468ce73c7fe62ca00f")

	depends_on("r@4.2:", type=("build", "run"))

	# annotation