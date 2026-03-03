# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlatowork(RPackage):
	"""Data from a Test of the PlatoWork tDCS Headset

	Data and analysis from an experiment with improving touch 
    typing speed, using the tDCS PlatoWork headset produced by PlatoScience.
	"""
	
	homepage = "https://github.com/lassehjorthmadsen/platowork"
	cran = "platowork" 

	version("0.0.1", md5="2eded2813db6c9b498979a73785ea6e5")

	depends_on("r@2.10:", type=("build", "run"))
