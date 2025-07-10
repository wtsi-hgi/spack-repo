# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsmb(RPackage):
	"""Data sets for the book 'Modern Statistics for Biology'

	Data sets for the book 'Modern Statistics for Modern Biology', S.P. Holmes and W. Huber.
	"""
	
	bioc = "MSMB" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/MSMB_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/MSMB/MSMB_1.20.0.tar.gz"]

	version("1.20.0", sha256="405b0ac8f361b5011c10c46786ce099660bc5584e5e9ef000101033fd8f109db")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))

