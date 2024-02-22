# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVennplot(RPackage):
	"""Venn Diagrams in 2D and 3D

	Calculate and plot Venn diagrams in 2D and 3D.
	"""
	
	cran = "vennplot" 

	version("1.0", md5="21768bf4ff420501e42fe24fb1e713dc")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
