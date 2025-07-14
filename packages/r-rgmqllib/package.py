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

	version("1.28.0", commit="939d464d010a829204657252c67b6394adc72d6c")
	version("1.22.0", commit="3dcb0286a3417357218a18e2c1898492fa155637")

	depends_on("r@3.4.2:", type=("build", "run"))

