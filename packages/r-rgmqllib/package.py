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

	version("1.22.0", sha256="9ed38960d0e55c3e80cd8480f0cf2c99aa6c36f704f90f4068b38213e546daeb")

	depends_on("r@3.4.2:", type=("build", "run"))

