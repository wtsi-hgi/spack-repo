# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlandr(RPackage):
	"""Bland-Altman Method Comparison

	Carries out Bland Altman analyses (also known as a Tukey
    mean-difference plot) as described by JM Bland and DG Altman in
    1986 <doi:10.1016/S0140-6736(86)90837-8>. This package was created in 
    2015 as existing Bland-Altman analysis functions did not calculate 
    confidence intervals. This package was created to rectify this, 
    and create reproducible plots. This package is also available as a module
    for the 'jamovi' statistical spreadsheet (see <https://www.jamovi.org>
    for more information).
	"""
	
	homepage = "https://github.com/deepankardatta/blandr/"
	cran = "blandr" 

	version("0.5.1", md5="717d43e78d3a9d66f332498d95296a8e")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-jmvcore@0.8.5:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("pandoc@1.12.3:", type=("build", "link", "run"))
