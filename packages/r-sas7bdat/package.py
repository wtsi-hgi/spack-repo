# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSas7bdat(RPackage):
	"""sas7bdat Reverse Engineering Documentation

	Documentation and prototypes for the earliest (circa 2010) open-source effort to reverse engineer the sas7bdat file format. The package includes a prototype reader for sas7bdat files. However, newer packages (notably the haven package) contain more robust readers for sas7bdat files.
	"""
	
	cran = "sas7bdat" 

	version("0.7", md5="74031cbc43efb2db578ff45a353a5e19")

	depends_on("r@2.10:", type=("build", "run"))
