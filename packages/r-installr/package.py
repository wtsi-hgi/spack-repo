# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInstallr(RPackage):
	"""Using R to Install Stuff on Windows OS (Such As: R, 'Rtools',
'RStudio', 'Git', and More!)

	R is great for installing software.  Through the 'installr'
    package you can automate the updating of R (on Windows, using updateR())
    and install new software. Software installation is initiated through a
    GUI (just run installr()), or through functions such as: install.Rtools(),
    install.pandoc(), install.git(), and many more. The updateR() command
    performs the following: finding the latest R version, downloading it,
    running the installer, deleting the installation file, copy and updating
    old packages to the new R installation.
	"""
	
	homepage = "https://talgalili.github.io/installr/"
	cran = "installr" 

	version("0.23.4", md5="2c3cddd895b3c8332430b2529be1b2b3")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
