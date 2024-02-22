# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPaperplanes(RPackage):
	"""Distance Recordings from a Paper Plane Folding/Flying Experiment

	This is a data only package, that provides distances from a paper plane experiment.
	"""
	
	homepage = "https://gitlab.gwdg.de/aleha/paperplanes"
	cran = "paperplanes" 

	version("0.0.1.9", md5="33c174afb4db7bed123e20fc33e3061b")

	depends_on("r@2.10:", type=("build", "run"))
