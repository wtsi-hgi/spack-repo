# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgmqllib(RPackage):
	"""RGMQLlib, java libraries to run GMQL scala API

	A package that contains scala libraries to call GMQL from R used by RGMQL package. It contains a scalable data management engine written in Scala programming language.
	"""
	
	homepage = "http://www.bioinformatics.deib.polimi.it/genomic_computing/GMQL/"
	bioc = "RGMQLlib" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/RGMQLlib_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/RGMQLlib/RGMQLlib_1.22.0.tar.gz"]

	version("1.22.0", md5="d8ad27b1fe0c5eff6135285db972cab2")

	depends_on("r@3.4.2:", type=("build", "run"))

	# experiment