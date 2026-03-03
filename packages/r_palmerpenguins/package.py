# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPalmerpenguins(RPackage):
	"""Palmer Archipelago (Antarctica) Penguin Data

	Size measurements, clutch observations, and blood isotope ratios for adult foraging Adélie, Chinstrap, and Gentoo penguins observed on islands in the Palmer Archipelago near Palmer Station, Antarctica. Data were collected and made available by Dr. Kristen Gorman and the Palmer Station Long Term Ecological Research (LTER) Program. 
	"""
	
	homepage = "https://allisonhorst.github.io/palmerpenguins/"
	cran = "palmerpenguins" 

	version("0.1.1", md5="dff628ed0c5f7b8e265127221491934e")

	depends_on("r@2.10:", type=("build", "run"))
