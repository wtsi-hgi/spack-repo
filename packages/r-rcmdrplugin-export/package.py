# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcmdrpluginExport(RPackage):
	"""Export R Output to LaTeX or HTML

	Export Rcmdr output to LaTeX or HTML code. The
        plug-in was originally intended to facilitate exporting Rcmdr
        output to formats other than ASCII text and to provide R
        novices with an easy-to-use, easy-to-access reference on
        exporting R objects to formats suited for printed output. The
        package documentation contains several pointers on creating
        reports, either by using conventional word processors or
        LaTeX/LyX.
	"""
	
	cran = "RcmdrPlugin.Export" 

	version("0.3-1", md5="7e40d7d64e20c429eed12c5ec0661e75")

	depends_on("r-rcmdr@2.2.2:", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
