# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGmt(RPackage):
	"""Interface Between GMT Map-Making Software and R

	Interface between the GMT map-making software and R, enabling the
  user to manipulate geographic data within R and call GMT commands to draw and
  annotate maps in postscript format. The gmt package is about interactive data
  analysis, rapidly visualizing subsets and summaries of geographic data, while
  performing statistical analysis in the R console.
	"""
	
	homepage = "https://www.generic-mapping-tools.org"
	cran = "gmt" 

	version("2.0.3", md5="eee5cfca7eac6741d9ac47506ca49de8")

	depends_on("gmt", type=("build", "link", "run"))
