# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpdesign(RPackage):
	"""Designing Stated Preference Experiments

	Contemporary software commonly used to design stated preference experiments are expensive and the code is closed source. This is a free software package with an easy to use interface to make flexible stated preference experimental designs using state-of-the-art methods. For an overview of stated choice experimental design theory, see e.g., Rose, J. M. & Bliemer, M. C. J. (2014) in Hess S. & Daly. A. <doi:10.4337/9781781003152>. The package website can be accessed at <https://spdesign.edsandorf.me>. We acknowledge funding from the European Union’s Horizon 2020 research and innovation program under the Marie Sklodowska-Curie grant INSPiRE (Grant agreement ID: 793163).
	"""
	
	homepage = "https://spdesign.edsandorf.me"
	cran = "spdesign" 

	version("0.0.3", md5="13b4f08ada5eebc11831026f5c67ba83")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-randtoolbox", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
