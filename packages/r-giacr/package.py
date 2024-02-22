# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGiacr(RPackage):
	"""Interface to the Computer Algebra System 'Giac'

	'Giac'
    <https://www-fourier.ujf-grenoble.fr/~parisse/giac/doc/en/cascmd_en/cascmd_en.html>
    is a general purpose symbolic algebra software. It powers the
    graphical interface 'Xcas'. This package allows to execute 'Giac'
    commands in 'R'.
	"""
	
	homepage = "https://github.com/stla/giacR"
	cran = "giacR" 

	version("1.0.0", md5="d52fe0f49591607033a0480534136e3c")

	depends_on("r-chromote@0.1.2:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-pingr", type=("build", "run"))
	depends_on("r-processx", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
