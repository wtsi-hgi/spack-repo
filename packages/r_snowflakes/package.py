# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnowflakes(RPackage):
	"""Random Snowflake Generator

	The function generates and plots random snowflakes. Each snowflake is defined by a given diameter, width of the crystal, color, and random seed. Snowflakes are plotted in such way that they always remain round, no matter what the aspect ratio of the plot is. Snowflakes can be created using transparent colors, which creates a more interesting, somewhat realistic, image. Images of the snowflakes can be separately saved as svg files and used in websites as static or animated images.
	"""
	
	cran = "snowflakes" 

	version("1.0.0", md5="4dfcc36e626897764d75b8748139e7e5")

	depends_on("r@3.1:", type=("build", "run"))
