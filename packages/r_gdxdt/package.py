# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGdxdt(RPackage):
	"""IO for GAMS GDX Files using 'data.table'

	Interfaces GAMS data (*.gdx) files with 'data.table's using the GAMS R package 'gdxrrw'. The 'gdxrrw' package is available on the GAMS wiki: <https://support.gams.com/doku.php?id=gdxrrw:interfacing_gams_and_r>.
	"""
	
	cran = "gdxdt" 

	version("0.1.0", md5="664250a8f3d9d1b0097d8b397fd988d5")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-data-table@1.11:", type=("build", "run"))
