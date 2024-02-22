# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElitism(RPackage):
	"""Equipment for Logarithmic and Linear Time Stepwise Multiple
Hypothesis Testing

	Recently many new p-value based multiple test procedures have been proposed, and these new methods are more powerful than the widely used Hochberg procedure. These procedures strongly control the familywise error rate (FWER). This is a comprehensive collection of p-value based FWER-control stepwise multiple test procedures, including six procedure families and thirty multiple test procedures. In this collection, the conservative Hochberg procedure, linear time Hommel procedures, asymptotic Rom procedure, Gou-Tamhane-Xi-Rom procedures, and Quick procedures are all developed in recent five years since 2014. The package name "elitism" is an acronym of "e"quipment for "l"ogarithmic and l"i"near "ti"me "s"tepwise "m"ultiple hypothesis testing.
    See Gou, J. (2022), "Quick multiple test procedures and p-value adjustments", Statistics in Biopharmaceutical Research 14(4), 636-650.
	"""
	
	cran = "elitism" 

	version("1.1.1", md5="424762eec20ce983d5f5a24fa7af4f57")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-mass@7:", type=("build", "run"))
