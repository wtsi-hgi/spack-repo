# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJavagd(RPackage):
	"""Java Graphics Device

	Graphics device routing all graphics commands to a Java
	     program. The actual functionality of the JavaGD depends
	     on the Java-side implementation. Simple AWT and Swing
	     implementations are included.
	"""
	
	homepage = "https://www.rforge.net/JavaGD/"
	cran = "JavaGD" 

	version("0.6-5", md5="fbd5362b8a3c1cf2e1d85af345ecda6c")

	depends_on("r@2.4:", type=("build", "run"))
	depends_on("r-rjava@0.5.0:", type=("build", "run"))
	depends_on("openjdk@1.2:", type=("build", "link", "run"))
